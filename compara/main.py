import logging
import os
from flask import Flask, jsonify, render_template, request

# 1. Configuración de Logging para trazabilidad profesional
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()],
)

# 2. Configuración explícita de rutas para evitar errores de despliegue
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR, "static")

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)


# 3. Manejadores globales de errores (Evita mostrar pantallas rojas o feas)
@app.errorhandler(404)
def not_found_error(error):
    return (
        jsonify({"error": "Recurso no encontrado. Revisa la URL ingresada."}),
        404,
    )


@app.errorhandler(500)
def internal_error(error):
    logging.error(f"Error interno del servidor: {error}")
    return jsonify({"error": "Ocurrió un error inesperado en el servidor."}), 500


# 4. Rutas principales
@app.route("/")
def home():
    """Sirve la interfaz gráfica."""
    return render_template("index.html")


@app.route("/api/comparar", methods=["GET"])
def comparar():
    """Endpoint de la API para comparar dos números enteros."""
    x_raw = request.args.get("x")
    y_raw = request.args.get("y")

    # Validación de parámetros requeridos
    if x_raw is None or y_raw is None:
        logging.warning("Petición rechazada: Faltan parámetros x o y.")
        return (
            jsonify({"error": "Debes proporcionar ambos parámetros: x e y."}),
            400,
        )

    # Validación de tipos de datos
    try:
        x = int(x_raw)
        y = int(y_raw)
    except ValueError:
        logging.warning(
            f"Petición rechazada: Datos no numéricos recibidos (x={x_raw}, y={y_raw})."
        )
        return (
            jsonify({"error": "Por favor ingresa números enteros válidos para x e y."}),
            400,
        )

    # Lógica de comparación
    if x > y:
        resultado = f"{x} es mayor que {y}"
    elif x < y:
        resultado = f"{x} es menor que {y}"
    else:
        resultado = f"{x} es igual a {y}"

    logging.info(f"Comparación realizada con éxito: x={x}, y={y}")
    return jsonify({"x": x, "y": y, "resultado": resultado}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
