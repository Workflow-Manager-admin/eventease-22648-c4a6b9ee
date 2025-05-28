from typing import Dict, List
from datetime import datetime
from .models import User, Event, Registration

# Simulated auto-increment
_USER_ID = 1
_EVENT_ID = 1
_REGISTRATION_ID = 1

users: Dict[int, User] = {}
events: Dict[int, Event] = {}
registrations: Dict[int, Registration] = {}

def get_next_user_id():
    global _USER_ID
    uid = _USER_ID
    _USER_ID += 1
    return uid

def get_next_event_id():
    global _EVENT_ID
    eid = _EVENT_ID
    _EVENT_ID += 1
    return eid

def get_next_registration_id():
    global _REGISTRATION_ID
    rid = _REGISTRATION_ID
    _REGISTRATION_ID += 1
    return rid

def get_user_by_username(username: str):
    return next((u for u in users.values() if u.username == username), None)

def get_user(user_id: int):
    return users.get(user_id)

def add_user(user: User):
    users[user.id] = user

def add_event(event: Event):
    events[event.id] = event

def get_event(event_id: int):
    return events.get(event_id)

def delete_event(event_id: int):
    return events.pop(event_id, None)

def add_registration(reg: Registration):
    registrations[reg.id] = reg

def get_user_registrations(user_id: int):
    return [r for r in registrations.values() if r.user_id == user_id]

def get_event_registrations(event_id: int):
    return [r for r in registrations.values() if r.event_id == event_id]

def get_registration(registration_id: int):
    return registrations.get(registration_id)

def delete_registration(registration_id: int):
    return registrations.pop(registration_id, None)
