import mysql.connector
from tabulate import tabulate
import os

print("Directorio actual:", os.getcwd())

# Establecer la conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="Magaly_PG",
    password="",
    database="rehabilitacion"
)

# Crear un cursor para ejecutar consultas
cursor = conexion.cursor()

try:
    # Consulta para seleccionar todos los registros de la tabla
    consulta = "SELECT * FROM datos_sensor ORDER BY id DESC LIMIT 100"
    
    # Ejecutar la consulta
    cursor.execute(consulta)
    
    # Recuperar todos los registros
    registros = cursor.fetchall()
    
    # Obtener los nombres de las columnas
    columnas = [i[0] for i in cursor.description]
    
    # Imprimir los registros de manera ordenada usando tabulate
    datos_tabla = tabulate(registros, headers=columnas, tablefmt="pretty")
    print(datos_tabla)
    
    # Guardar los datos en un archivo de texto
    with open("registros_datos_sensor.txt", "w") as archivo:
        archivo.write(datos_tabla)
        print("Datos guardados en 'registros_datos_sensor.txt'")
    
except mysql.connector.Error as error:
    print("Error al ejecutar la consulta:", error)

finally:
    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()
