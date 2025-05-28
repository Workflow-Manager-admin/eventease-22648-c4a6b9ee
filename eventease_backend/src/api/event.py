from fastapi import APIRouter, HTTPException, Depends, status
from typing import List
from datetime import datetime
from . import schemas, database, models, auth

router = APIRouter(prefix="/events", tags=["events"])

@router.get("/", response_model=List[schemas.EventOut])
def list_events():
    """Return all events (upcoming and past)."""
    return list(database.events.values())

@router.get("/{event_id}", response_model=schemas.EventOut)
def get_event(event_id: int):
    event = database.get_event(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.post("/", response_model=schemas.EventOut, status_code=201, dependencies=[Depends(auth.require_admin)])
def create_event(event: schemas.EventCreate):
    eid = database.get_next_event_id()
    event_obj = models.Event(
        id=eid,
        name=event.name,
        description=event.description,
        date=event.date,
        location=event.location,
        capacity=event.capacity
    )
    database.add_event(event_obj)
    return event_obj

@router.put("/{event_id}", response_model=schemas.EventOut, dependencies=[Depends(auth.require_admin)])
def update_event(event_id: int, event: schemas.EventCreate):
    event_obj = database.get_event(event_id)
    if not event_obj:
        raise HTTPException(status_code=404, detail="Event not found")
    event_obj.name = event.name
    event_obj.description = event.description
    event_obj.date = event.date
    event_obj.location = event.location
    event_obj.capacity = event.capacity
    database.add_event(event_obj)
    return event_obj

@router.delete("/{event_id}", status_code=204, dependencies=[Depends(auth.require_admin)])
def delete_event(event_id: int):
    removed = database.delete_event(event_id)
    if not removed:
        raise HTTPException(status_code=404, detail="Event not found")
    return
