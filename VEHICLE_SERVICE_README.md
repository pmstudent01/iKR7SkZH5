# Vehicle Service API (Python / Flask)

A Python implementation of the **Vehicle Service Collection** API. The response
shapes, status codes and error messages mirror the examples saved in the Postman
collection.

## Project structure

```
app/
  __init__.py
  app.py       # Flask application factory + entry point
  routes.py    # Vehicle endpoints
  store.py     # In-memory, thread-safe vehicle store (seeded with sample data)
run.py         # `python run.py` to start the server
requirements.txt
```

## Setup

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
```

## Run

```bash
python run.py
```

The server starts on `http://localhost:3000`.

Point your Postman environment's `baseUrl` variable at `http://localhost:3000`
to run the Vehicle Service Collection against this app.

## Endpoints

| Method | Path             | Description        | Success |
|--------|------------------|--------------------|---------|
| GET    | `/vehicles`      | List all vehicles  | `200`   |
| POST   | `/vehicles`      | Create a vehicle   | `201`   |
| GET    | `/vehicles/<id>` | Retrieve a vehicle | `200`   |
| PATCH  | `/vehicles/<id>` | Update a vehicle   | `200`   |
| DELETE | `/vehicles/<id>` | Delete a vehicle   | `204`   |
| GET    | `/health`        | Health check       | `200`   |

### Error responses

| Status | When                                            |
|--------|-------------------------------------------------|
| `400`  | Create request missing a required attribute     |
| `404`  | Vehicle with the given id does not exist        |
| `409`  | A vehicle with the same VIN already exists       |

### Vehicle object

```json
{
  "id": 1,
  "nickName": "The Lisa Marie",
  "vin": "4M2DV11W4RDJ53329",
  "make": "Mercury",
  "model": "Villager",
  "year": "1994",
  "miles": 159864
}
```

The store is seeded with two vehicles (ids `1` and `2`) so the collection's
example requests work immediately.
