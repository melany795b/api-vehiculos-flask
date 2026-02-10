def listar_vehiculos(conexion): # Función para recibir conexión activa a MySQL
    lista = []  # Lista para guardar los vehículos obtenidos

    # dictionary=True hace que los resultados vengan como diccionarios (JSON friendly)
    cursor = conexion.cursor(dictionary=True)

    # Llamada al P.A.que recupera los vehículos
    sql = "CALL CC_sp_listar_vehiculo()"
    cursor.execute(sql)

    # Recorremos cada fila devuelta por la base de datos
    for row in cursor:
        lista.append(row)  # Agregamos cada vehículo a la lista

    cursor.close()  # Cerramos el cursor (buena práctica)

    return lista  # Devuelve la lista de vehiculs

def obtener_vehiculo_por_id(conexion, vehiculo_id):
    # Cursor en formato diccionario
    cursor = conexion.cursor(dictionary=True)

    # Llamamos al procedimiento con parámetro
    sql = "CALL CC_sp_obtener_vehiculo_por_id(%s)"
    cursor.execute(sql, (vehiculo_id,))

    # Solo queremos UN registro
    vehiculo = cursor.fetchone()

    cursor.close()

    return vehiculo
