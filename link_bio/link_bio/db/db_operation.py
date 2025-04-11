from link_bio.db.db_connection  import create_connection
import mysql.connector
from mysql.connector import Error
import mysql.connector

def obtener_pacientes():
    """Obtiene todos los pacientes de la base de datos"""
    connection = create_connection()
    if not connection:
        return None
    
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM pacientes")
        pacientes = cursor.fetchall()
        return pacientes
        
    except Error as e:
        print(f"Error al obtener pacientes: {e}")
        return None
        
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

# Insertar un nuevo paciente en la base de datos
def insertar_paciente(id: str, nombre: str, edad: int, observaciones: str, deporte: str, estado_tratamiento: str, fecha_ultima_consulta: str):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO pacientes (id,nombre, edad, observaciones, deporte, estado_tratamiento, fecha_ultima_consulta) VALUES (%s,%s, %s, %s, %s, %s, %s)",
        (id,nombre, edad, observaciones, deporte, estado_tratamiento, fecha_ultima_consulta)
    )
    conn.commit()
    conn.close()


