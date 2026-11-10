"""In-memory data store for vehicles.

Seeded with the sample data used across the Vehicle Service Collection
examples so the generated API matches the documented responses out of the box.
"""

from threading import Lock
from typing import Dict, List, Optional


class VehicleStore:
    """A simple thread-safe in-memory vehicle store."""

    def __init__(self) -> None:
        self._lock = Lock()
        self._vehicles: Dict[int, dict] = {}
        self._next_id = 1
        self._seed()

    def _seed(self) -> None:
        seed_data = [
            {
                "nickName": "The Lisa Marie",
                "vin": "4M2DV11W4RDJ53329",
                "make": "Mercury",
                "model": "Villager",
                "year": "1994",
                "miles": 159864,
            },
            {
                "nickName": "Dolly",
                "vin": "JN8AZ2KR1AT169594",
                "make": "Nissan",
                "model": "Cube",
                "year": "2010",
                "miles": 59000,
            },
        ]
        for item in seed_data:
            self._insert(item)

    def _insert(self, data: dict) -> dict:
        vehicle = {"id": self._next_id, **data}
        self._vehicles[self._next_id] = vehicle
        self._next_id += 1
        return vehicle

    def list_all(self) -> List[dict]:
        with self._lock:
            return list(self._vehicles.values())

    def get(self, vehicle_id: int) -> Optional[dict]:
        with self._lock:
            return self._vehicles.get(vehicle_id)

    def find_by_vin(self, vin: str) -> Optional[dict]:
        with self._lock:
            for vehicle in self._vehicles.values():
                if vehicle.get("vin") == vin:
                    return vehicle
        return None

    def create(self, data: dict) -> dict:
        with self._lock:
            return self._insert(data)

    def update(self, vehicle_id: int, data: dict) -> Optional[dict]:
        with self._lock:
            vehicle = self._vehicles.get(vehicle_id)
            if vehicle is None:
                return None
            for key in ("nickName", "vin", "make", "model", "year", "miles"):
                if key in data:
                    vehicle[key] = data[key]
            return vehicle

    def delete(self, vehicle_id: int) -> bool:
        with self._lock:
            return self._vehicles.pop(vehicle_id, None) is not None


# Module-level singleton used by the app.
store = VehicleStore()
