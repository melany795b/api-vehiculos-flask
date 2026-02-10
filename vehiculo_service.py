# Importamos la función de conexión
from database import get_connection

# Importamos la función DAO que consulta los vehículos
from vehiculo_dao import listar_vehiculos, obtener_vehiculo_por_id

# Función que maneja la lógica de negocio
def obtener_vehiculos():
    conexion = get_connection()  # Abrimos conexión a la base

    try:
        # Llamamos al DAO para obtener los datos
        return listar_vehiculos(conexion)
    finally:
        # Pase lo que pase, cerramos la conexión
        conexion.close()

# Funcion para obtener un vehiculo por su id
def obtener_vehiculo_id(vehiculo_id):
    # Se abre una nueva conexión a la base de datos
    conexion = get_connection()

    try:
        # Llamamos al DAO enviándole:
        # 1) la conexión activa
        # 2) el ID que vino desde el endpoint
        # El DAO ejecuta el procedimiento almacenado con ese ID
        return obtener_vehiculo_por_id(conexion, vehiculo_id)

    finally:
        # Cerramos la conexión siempre (buena práctica)
        conexion.close()

