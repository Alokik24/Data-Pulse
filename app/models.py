from enum import Enum
from typing import Dict
from pydantic import BaseModel, Field, field_validator
import re

# Allowed event names
class EventName(str, Enum):
    signup = "signup"
    login = "login"
    click = "click"
    purchase = "purschase"

# Input Schema
class Event(BaseModel):
    name: EventName
    user_id: str = Field(..., min_length=3, max_length=30, description="User ID must be between 3-30 characters")
    properties: Dict[str, str] = Field(default_factory=dict)

    @field_validator('user_id')
    def validate_user_id(cls, v):
        if not re.match(r'^[a-zA-Z0-9_\-]+$', v):
            raise ValueError('User ID must be alphanumeric with optional _ or -')
        return v