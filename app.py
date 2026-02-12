from flask import Flask
from rutas.rutas_vehiculo import vehiculo_bp

app = Flask(__name__)

# Registramos las rutas del módulo vehiculo
app.register_blueprint(vehiculo_bp)

# Punto de inicio del servidor
if __name__ == '__main__':
    app.run(debug=True)