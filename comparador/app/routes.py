import logging
from flask import Blueprint, jsonify, render_template, request
from app.services import ComparadorService

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def home():
    """Sirve la interfaz web principal."""
    return render_template("index.html")


@main_bp.route("/api/comparar", methods=["GET"])
def comparar():
    """Endpoint RESTful para comparar dos números."""
    x_raw = request.args.get("x")
    y_raw = request.args.get("y")

    if x_raw is None or y_raw is None:
        logging.warning("Parámetros insuficientes recibidos en /api/comparar")
        return (
            jsonify({"error": "Debes proporcionar ambos parámetros: x e y."}),
            400,
        )

    try:
        x = int(x_raw)
        y = int(y_raw)
    except ValueError:
        logging.warning(f"Error de conversión con valores: x={x_raw}, y={y_raw}")
        return (
            jsonify({"error": "Por favor ingresa números enteros válidos para x e y."}),
            400,
        )

    # Invocación de la capa de servicio
    resultado = ComparadorService.comparar_enteros(x, y)
    logging.info(f"Comparación procesada con éxito: {x} vs {y}")

    return jsonify({"x": x, "y": y, "resultado": resultado}), 200
