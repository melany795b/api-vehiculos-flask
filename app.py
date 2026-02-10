from flask import Flask, jsonify, request
from vehiculo_service import obtener_vehiculos, obtener_vehiculo_id
import json
import os

# Creamos la aplicación web Flask
app = Flask(__name__)

# Carpeta donde se guardarán los archivos JSON (cache)
CACHE_FOLDER = "cache_vehiculos"

# Archivo donde se guarda la lista completa de vehículos
CACHE_FILE = os.path.join(CACHE_FOLDER, "vehiculos.json")


# Listar vehiculos
@app.route('/vehiculos', methods=['GET'])
def vehiculos():
    # Leemos parámetro de la url
    accion = request.args.get("accion")

    if accion == "listar":
        # Llamamos al service para obtener los datos desde la BD
        lista = obtener_vehiculos()

        # Si la carpeta de cache no existe, se crea
        if not os.path.exists(CACHE_FOLDER):
            os.makedirs(CACHE_FOLDER)

        # Guardamos los datos en un archivo json
        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(lista, f, ensure_ascii=False, indent=4)

        # Devolvemos los datos en formato json al navegador
        return jsonify(lista)

    else:
        # Error si no se reconoce la acción
        return jsonify({"error": "Acción no reconocida"}), 400

# obtener vehiculo por id
@app.route('/vehiculos/<int:id>', methods=['GET'])
def vehiculo_por_id(id):
    # Llamamos al service enviando el id
    vehiculo = obtener_vehiculo_id(id)

    # Si el vehículo existe en la base de datos
    if vehiculo:

        # Crear carpeta si no existe
        if not os.path.exists(CACHE_FOLDER):
            os.makedirs(CACHE_FOLDER)

        # Archivo json individual por vehículo
        ruta_individual = os.path.join(CACHE_FOLDER, f"vehiculo_{id}.json")

        # Guardamos el resultado en json
        with open(ruta_individual, "w", encoding="utf-8") as f:
            json.dump(vehiculo, f, ensure_ascii=False, indent=4)

        # Retornamos el vehículo al cliente
        return jsonify(vehiculo)

    else:
        # Si no se encuentra el id
        return jsonify({"error": "Vehículo no encontrado"}), 404


# Punto de inicio del programa 
if __name__ == '__main__':
    app.run(debug=True)

