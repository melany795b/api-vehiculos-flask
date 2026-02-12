# Importamos función de conexión
from database import get_connection

# Importamos función DAO (consulta de vehículos)
from vehiculo_dao import listar_vehiculos, obtener_vehiculo_por_id

# Función que maneja la lógica de negocio
def obtener_vehiculos():
    conexion = get_connection()

    try:
        return listar_vehiculos(conexion)
    finally:
        conexion.close()

# Funcion para obtener un vehiculo por su id
def obtener_vehiculo_id(vehiculo_id):
    conexion = get_connection()

    try:
        return obtener_vehiculo_por_id(conexion, vehiculo_id)

    finally:
        conexion.close()
close()

