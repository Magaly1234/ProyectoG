import mysql.connector
from mysql.connector import Error

def create_connection():
    """Crea y retorna una conexión a la base de datos"""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='Magaly_PG',
            password='',
            database='rehabilitacion'
        )
        
        if connection.is_connected():
            print("✅ Conexión establecida correctamente")
            return connection
            
    except Error as e:
        print(f"❌ Error al conectar a MySQL: {e}")
        return None