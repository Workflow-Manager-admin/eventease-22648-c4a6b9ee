from typing import Optional, List, Dict
from pydantic import BaseModel, Field
from datetime import datetime

# USER AUTH


# PUBLIC_INTERFACE
class UserCreate(BaseModel):
    username: str
    password: str

# PUBLIC_INTERFACE
class UserLogin(BaseModel):
    username: str
    password: str

# PUBLIC_INTERFACE
class UserOut(BaseModel):
    id: int
    username: str
    is_admin: bool

# EVENT SCHEMAS

# PUBLIC_INTERFACE
class EventCreate(BaseModel):
    name: str
    description: Optional[str] = None
    date: datetime
    location: Optional[str] = None
    capacity: Optional[int] = Field(default=None, ge=1)

# PUBLIC_INTERFACE
class EventOut(BaseModel):
    id: int
    name: str
    description: Optional[str]
    date: datetime
    location: Optional[str]
    capacity: Optional[int]

# REGISTRATION SCHEMAS

# PUBLIC_INTERFACE
class RegistrationCreate(BaseModel):
    event_id: int
    form_data: Dict[str, str]

# PUBLIC_INTERFACE
class RegistrationOut(BaseModel):
    id: int
    event_id: int
    user_id: int
    registration_time: datetime
    form_data: Dict[str, str]
