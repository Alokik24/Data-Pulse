from fastapi import APIRouter, status
from app.models import Event
from app.schemas import IngestResponse

router = APIRouter()

@router.post("/ingest", response_model=IngestResponse, status_code=status.HTTP_202_ACCEPTED)
async def ingest(event: Event):
    print(f"[LOG] Received Event: {event.model_dump_json()}")
    return {"status": "accepted", "received_event": event}
