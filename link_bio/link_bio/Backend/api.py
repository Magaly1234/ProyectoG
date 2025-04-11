from fastapi import FastAPI, WebSocket
import mysql.connector
import asyncio
import numpy as np
from scipy.spatial.transform import Rotation as R
from fastapi.middleware.cors import CORSMiddleware
from starlette.websockets import WebSocketDisconnect

app = FastAPI()

# Middleware para permitir CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes cambiar "" por los dominios específicos
    allow_credentials=True,
    allow_methods=["*"],  # Se pueden especificar métodos permitidos
    allow_headers=["*"],  # Se pueden especificar encabezados permitidos
)

# Función para obtener los últimos datos desde MySQL
def obtener_datos():
    conexion = mysql.connector.connect(
        host="localhost",
        user="Magaly_PG",
        password="",
        database="rehabilitacion"
    )
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM datos_sensor ORDER BY id DESC LIMIT 1")
    datos = cursor.fetchone()
    cursor.close()
    conexion.close()
    return datos

def guardar_angulos(paciente_id, dorsiflexion, abduccion, inversion):
    try:
        # Convertir valores NumPy a tipos nativos de Python
        dorsiflexion_val = float(dorsiflexion)
        abduccion_val = float(abduccion)
        inversion_val = float(inversion)
        
        
        
        print("ID del paciente recibido:", paciente_id)  # <-- AQUI
        conexion = mysql.connector.connect(
            host="localhost",
            user="Magaly_PG",
            password="",
            database="rehabilitacion"
        )
        cursor = conexion.cursor()
        
        # Consulta SQL para insertar los ángulos
        query = """
        INSERT INTO angulos_movimiento 
        (paciente_id, dorsiflexion, abduccion, inversion, fecha_registro) 
        VALUES (%s, %s, %s, %s, NOW())
        """
        valores = (paciente_id, dorsiflexion_val, abduccion_val, inversion_val)
        
        cursor.execute(query, valores)
        conexion.commit()
        
        cursor.close()
        
        
        return True
    except Exception as e:
        print(f"Error al guardar ángulos: {e}")
        return False
    
# operaciones para obtener mis variables biomecanicas  


# Función para normalizar un vector
def normalizar(v):
    norm = np.linalg.norm(v)
    return v / norm if norm != 0 else v

# Función para calcular ángulos con acelerómetro y giroscopio (fusión de sensores)
def calcular_angulos(datos):
    if not datos:
        return {"dorsiflexion": 0, "abduccion": 0, "inversion": 0}

    # Extraer datos de aceleración y giroscopio
    ax1, ay1, az1 = datos['aceleracion_x1'], datos['aceleracion_y1'], datos['aceleracion_z1']
    ax2, ay2, az2 = datos['aceleracion_x2'], datos['aceleracion_y2'], datos['aceleracion_z2']
    gx1, gy1, gz1 = datos['giroscopio_x1'], datos['giroscopio_y1'], datos['giroscopio_z1']
    gx2, gy2, gz2 = datos['giroscopio_x2'], datos['giroscopio_y2'], datos['giroscopio_z2']

    # Normalizar vectores de aceleración
    acc1 = normalizar(np.array([ax1, ay1, az1]))
    acc2 = normalizar(np.array([ax2, ay2, az2]))

    # Calcular orientación con acelerómetro (ángulos iniciales)
    ang_acc1 = np.arctan2(acc1[1], acc1[2]) * (180 / np.pi), np.arctan2(-acc1[0], np.sqrt(acc1[1]**2 + acc1[2]**2)) * (180 / np.pi)
    ang_acc2 = np.arctan2(acc2[1], acc2[2]) * (180 / np.pi), np.arctan2(-acc2[0], np.sqrt(acc2[1]**2 + acc2[2]**2)) * (180 / np.pi)

    # Convertir giroscopio a cuaterniones
    rot1 = R.from_euler('xyz', [gx1, gy1, gz1], degrees=True)
    rot2 = R.from_euler('xyz', [gx2, gy2, gz2], degrees=True)

    # Convertir a ángulos de Euler
    angulos1 = rot1.as_euler('xyz', degrees=True)
    angulos2 = rot2.as_euler('xyz', degrees=True)

    # Promedio ponderado entre acelerómetro y giroscopio (fusión de sensores)
    alpha = 0.98  # Peso del giroscopio (ajustable)
    dorsiflexion = alpha * (angulos2[0] - angulos1[0]) + (1 - alpha) * (ang_acc2[0] - ang_acc1[0])
    abduccion = alpha * (angulos2[1] - angulos1[1]) + (1 - alpha) * (ang_acc2[1] - ang_acc1[1])
    inversion = alpha * (angulos2[2] - angulos1[2])

    return {"dorsiflexion": dorsiflexion, "abduccion": abduccion, "inversion": inversion}

# Nueva ruta HTTP para obtener datos manualmente
@app.get("/datos")
def obtener_datos_api():
    datos = obtener_datos()
    angulos = calcular_angulos(datos)
    if datos:
        guardar_angulos(datos['id'], angulos['dorsiflexion'], angulos['abduccion'], angulos['inversion'])
    
    return {"datos": datos, "angulos": angulos}

# WebSocket para enviar datos en tiempo real
@app.websocket("/ws/datos")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            datos = obtener_datos()
            angulos = calcular_angulos(datos)

            if not datos:
                await websocket.send_json({"error": "No hay datos disponibles"})
            else:
                guardar_angulos(datos['id'], angulos['dorsiflexion'], angulos['abduccion'], angulos['inversion'])
                
                await websocket.send_json({"datos": datos, "angulos": angulos})
            
            await asyncio.sleep(1)

    except WebSocketDisconnect:
        print("Cliente WebSocket desconectado")
    except Exception as e:
        print(f"Error en WebSocket: {e}")
    finally:
        await websocket.close()
