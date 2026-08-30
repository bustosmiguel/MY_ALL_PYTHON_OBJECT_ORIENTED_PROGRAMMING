import logging
import os
from flask import Flask, jsonify


def create_app():
    """Inicializa y configura la aplicación mediante Application Factory Pattern."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    app = Flask(
        __name__,
        template_folder=os.path.join(base_dir, "templates"),
        static_folder=os.path.join(base_dir, "static"),
    )

    # Configuración de Logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

    # Registro de Blueprints
    from app.routes import main_bp

    app.register_blueprint(main_bp)

    # Manejadores de Errores
    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"error": "Recurso no encontrado"}), 404

    @app.errorhandler(500)
    def server_error(e):
        logging.error(f"Error crítico de servidor: {e}")
        return jsonify({"error": "Error interno del servidor"}), 500

    return app
