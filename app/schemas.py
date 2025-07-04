from pydantic import BaseModel
from app.models import Event

# Output Schema
class IngestResponse(BaseModel):
    status: str
    received_event: Event