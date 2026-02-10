print(">>> CARGANDO database.py")
import mysql.connector #librería para conectar Python a MySQL

# Función que crea y devuelve una conexión a la base de datos
def get_connection():
    return mysql.connector.connect(
        host="localhost",          # Dirección del servidor MySQL
        port=3306,                 # Puerto de MySQL 
        user="root",               # Usuario de la bd
        password="root",           # Contraseña de la bd
        database="bdvalescombustible"  # Nombre de la bd
    )
