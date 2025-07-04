# Data Pulse
**A minimal real-time analytics backend built with FastAPI + SQLite + Redis.**

---

## Goal

Track and analyze real-time user events like signups, logins, clicks, and purchases using a lightweight, modular backend.

## Tech Stack

| Layer         | Technology     |
|---------------|----------------|
| API Framework | FastAPI        |
| Validation    | Pydantic       |
| Storage       | SQLite (→ TimescaleDB) |
| Real-Time Ops | Redis          |
| Dashboard     | Streamlit      |
| Container     | Docker         |

---

## Event Schema and Validation
### Event Model
Event ingestion is strictly validated using [Pydantic](https://docs.pydantic.dev/).

## Model
| Field       | Type   | Validation Rules                                                  |
|-------------|--------|--------------------------------------------------------------------|
| `name`      | Enum   | Must be one of: `signup`, `login`, `click`, `purchase`            |
| `user_id`   | String | 3–30 characters, regex: `^[a-zA-Z0-9_-]+$`                         |
| `properties`| Dict   | Optional. Key-value string pairs for contextual metadata          |

## Valid Example
```json
{
  "name": "signup",
  "user_id": "user_42",
  "properties": {
    "source": "landing_page",
    "referrer": "google"
  }
}
```

## Invalid Example (bad ```user_id```)
```json
 {
  "name": "login",
  "user_id": "user@42"
}
```
### Returns:
```json
{
  "detail": [
    {
      "loc": ["body", "user_id"],
      "msg": "user_id must be alphanumeric with optional _ or -",
      "type": "value_error"
    }
  ]
}
```

## API Endpoint

``` POST /ingest```

Ingest an event into the pipeline. Currently logs the event (to be persisted on Day 4).

### Request
``` bash
curl -X POST http://localhost:8000/ingest \
-H "Content-Type: application/json" \
-d '{"name":"signup", "user_id":"abc_123", "properties":{"ref":"linkedin"}}'
```

### Response
```json
{
  "status": "accepted",
  "received_event": {
    "name": "signup",
    "user_id": "abc_123",
    "properties": {
      "ref": "linkedin"
    }
  }
}

```


## Milestones
- [x] Day 1: Project setup & base FastAPI app
- [x] Day 2: Schema + validation using Pydantic
- [x] Day 3: /ingest endpoint with 202 response + structured logging
- [ ] Day 4: Async SQLite storage (aiosqlite)
- [ ] Day 5: Pytest coverage + edge case testing
- [ ] Day 6+: Redis counter, background worker
- [ ] Week 2: TimescaleDB, Streamlit dashboard, Docker, Observability  

## Project Structure
```
data-pulse/
│
├── app/
│   ├── main.py        # FastAPI app entry point
│   ├── models.py      # Pydantic input schemas (Event)
│   ├── schemas.py     # Output/response schemas
│   └── routes.py      # API routes (POST /ingest)
│
├── requirements.txt   # Python dependencies
├── README.md          # Project documentation
├── .venv/             # Virtual environment (excluded in .gitignore)

```

## Resources
- [FastAPI docs](https://fastapi.tiangolo.com/)

- [Pydantic](https://docs.pydantic.dev/)

- [Uvicorn (ASGI Server)](https://www.uvicorn.org/)

## Author note
This project is part of a backend system design & full-stack AI learning path focused on building production-grade systems from scratch using Python-native tools.