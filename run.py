"""Convenience entry point: `python run.py` starts the Vehicle Service API."""

from app.app import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
