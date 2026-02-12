from flask import Blueprint, jsonify, request
from vehiculo_service import obtener_vehiculos, obtener_vehiculo_id
import json
import os

# Blueprint (mini app dentro de Flask)
vehiculo_bp = Blueprint('vehiculo_bp', __name__)

CACHE_FOLDER = "cache_vehiculos"
CACHE_FILE = os.path.join(CACHE_FOLDER, "vehiculos.json")

# Listar
@vehiculo_bp.route('/vehiculos', methods=['GET'])
def listar_vehiculos_controller():
    accion = request.args.get("accion")

    if accion == "listar":
        lista = obtener_vehiculos()

        if not os.path.exists(CACHE_FOLDER):
            os.makedirs(CACHE_FOLDER)

        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(lista, f, ensure_ascii=False, indent=4)

        return jsonify(lista)

    return jsonify({"error": "Acción no reconocida"}), 400

# Vehiculo por ID
@vehiculo_bp.route('/vehiculos/<int:id>', methods=['GET'])
def vehiculo_por_id_controller(id):
    vehiculo = obtener_vehiculo_id(id)

    if vehiculo:
        if not os.path.exists(CACHE_FOLDER):
            os.makedirs(CACHE_FOLDER)

        ruta = os.path.join(CACHE_FOLDER, f"vehiculo_{id}.json")

        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(vehiculo, f, ensure_ascii=False, indent=4)

        return jsonify(vehiculo)

    return jsonify({"error": "Vehículo no encontrado"}), 404
