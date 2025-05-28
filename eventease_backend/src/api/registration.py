from fastapi import APIRouter, HTTPException, Depends, status
from typing import List
from datetime import datetime
from . import schemas, database, models, auth

router = APIRouter(prefix="/registrations", tags=["registrations"])

@router.post("/", response_model=schemas.RegistrationOut, status_code=201)
def register(
    reg: schemas.RegistrationCreate,
    user: models.User = Depends(auth.get_current_user)
):
    event = database.get_event(reg.event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    # Enforce capacity if set
    registrations = database.get_event_registrations(reg.event_id)
    if event.capacity is not None and len(registrations) >= event.capacity:
        raise HTTPException(status_code=400, detail="Event capacity reached")
    for existing in registrations:
        if existing.user_id == user.id:
            raise HTTPException(status_code=400, detail="User already registered for this event")

    reg_id = database.get_next_registration_id()
    reg_obj = models.Registration(
        id=reg_id,
        user_id=user.id,
        event_id=reg.event_id,
        registration_time=datetime.utcnow(),
        form_data=reg.form_data or {},
    )
    database.add_registration(reg_obj)
    return reg_obj

@router.get("/mine", response_model=List[schemas.RegistrationOut])
def my_registrations(user: models.User = Depends(auth.get_current_user)):
    regs = database.get_user_registrations(user.id)
    return regs
