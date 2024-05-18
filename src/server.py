from fastapi import FastAPI, Depends
from src.schemas import schema
from src.infra.sqlalchemy.repositories import repository 
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db,create_database
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware import Middleware

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
]

app = FastAPI(middleware=middleware)
create_database()

@app.post("/events")
def create_event(event: schema.Event, db: Session = Depends(get_db)):
    created_event = repository.Event(db).create(event)
    return created_event

@app.get("/events")
def get_all_events_by_month(db: Session = Depends(get_db)):
    events = repository.Event(db).get_all_events_by_month()
    return events

@app.delete("/events/{eventId}")
def delete_event(eventId: int, db: Session = Depends(get_db)):
    deleted_event = repository.Event(db).remove(eventId)
    
    return deleted_event

@app.delete("/events/Month/{eventsdayInMonth}")
def delete_all_events_by_month(eventsdayInMonth: int, db: Session = Depends(get_db)):
    deleted_events = repository.Event(db).remove_by_month(eventsdayInMonth)
    return deleted_events

@app.put("/events/{eventId}")
def update_all_event_atributtes(eventId: int, event: schema.Event, db: Session = Depends(get_db)):
    updated_event = repository.Event(db).update_all_event_atributtes(eventId, event)
    return updated_event

@app.put("/events/Atributtes/{eventId}")
def update_specific_event_atributtes(eventId: int, event: schema.EventSA, db: Session = Depends(get_db)):
    updated_event = repository.Event(db).update_specific_event_atributtes(eventId, event)
    return updated_event

@app.put("/events/Done/{eventId}")
def update_is_done(eventId: int, db: Session = Depends(get_db)):
    updated_event = repository.Event(db).update_is_done(eventId)
    return updated_event

@app.put("/events/Cancelled/{eventId}")
def update_is_cancelled(eventId: int, db: Session = Depends(get_db)):
    updated_event = repository.Event(db).update_is_cancelled(eventId)
    return updated_event