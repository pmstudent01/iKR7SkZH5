"""Application factory and entry point for the Vehicle Service API."""

from flask import Flask, jsonify

from .routes import bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(bp)

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"}), 200

    @app.errorhandler(404)
    def not_found(_error):
        return jsonify({"message": "Resource not found."}), 404

    @app.errorhandler(500)
    def server_error(_error):
        return jsonify({"message": "Unexpected error."}), 500

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
