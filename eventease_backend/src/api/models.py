from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime


# PUBLIC_INTERFACE
class User(BaseModel):
    """User model for authentication and role management."""
    id: int
    username: str
    password_hash: str
    is_admin: bool


# PUBLIC_INTERFACE
class Event(BaseModel):
    """Event model describing event information."""
    id: int
    name: str
    description: Optional[str] = None
    date: datetime
    location: Optional[str] = None
    capacity: Optional[int] = None


# PUBLIC_INTERFACE
class Registration(BaseModel):
    """Model for user-event registration."""
    id: int
    user_id: int
    event_id: int
    registration_time: datetime
    form_data: dict  # To allow for arbitrary form fields per event
