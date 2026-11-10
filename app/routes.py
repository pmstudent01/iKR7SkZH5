"""HTTP routes for the Vehicle Service API.

Implements the endpoints documented in the Vehicle Service Collection:

    GET    /vehicles        List all vehicles
    POST   /vehicles        Create a vehicle
    GET    /vehicles/<id>   Retrieve a vehicle
    PATCH  /vehicles/<id>   Update a vehicle
    DELETE /vehicles/<id>   Delete a vehicle

Response shapes, status codes and error messages mirror the collection's
saved examples.
"""

from flask import Blueprint, jsonify, request

from .store import store

bp = Blueprint("vehicles", __name__)

REQUIRED_ATTRIBUTES = ["nickName", "vin", "make", "model", "year", "miles"]


def _error(message: str, status: int):
    return jsonify({"message": message}), status


@bp.get("/vehicles")
def list_vehicles():
    return jsonify(store.list_all()), 200


@bp.post("/vehicles")
def create_vehicle():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return _error("Request body must be a valid JSON object.", 400)

    # Validate required attributes (matches the 400 example).
    for attribute in REQUIRED_ATTRIBUTES:
        if attribute not in data or data[attribute] in (None, ""):
            return _error(
                f"Request body missing required attribute: {attribute}", 400
            )

    # Reject duplicate VINs (matches the 409 example).
    existing = store.find_by_vin(data["vin"])
    if existing is not None:
        return _error(
            f"Vehicle with VIN {data['vin']} already exists. "
            f"Existing vehicle ID: {existing['id']}",
            409,
        )

    vehicle = store.create(
        {attribute: data[attribute] for attribute in REQUIRED_ATTRIBUTES}
    )
    return jsonify(vehicle), 201


@bp.get("/vehicles/<int:vehicle_id>")
def retrieve_vehicle(vehicle_id: int):
    vehicle = store.get(vehicle_id)
    if vehicle is None:
        return _error(f"Vehicle with id: {vehicle_id} not found.", 404)
    return jsonify(vehicle), 200


@bp.patch("/vehicles/<int:vehicle_id>")
def update_vehicle(vehicle_id: int):
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return _error("Request body must be a valid JSON object.", 400)

    vehicle = store.update(vehicle_id, data)
    if vehicle is None:
        return _error(f"Vehicle with id: {vehicle_id} not found.", 404)
    return jsonify(vehicle), 200


@bp.delete("/vehicles/<int:vehicle_id>")
def delete_vehicle(vehicle_id: int):
    deleted = store.delete(vehicle_id)
    if not deleted:
        return _error(f"Vehicle with id: {vehicle_id} not found.", 404)
    return "", 204
