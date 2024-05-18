from sqlalchemy.orm import Session
from src.schemas import schema
from src.infra.sqlalchemy.models import models
from collections import defaultdict
import calendar

class Event():
    
    def __init__(self,db: Session):
        self.db=db
    
    def create(self, event: schema.Event):
        db_event = models.Event(    id = event.id,
                                    name=event.name, 
                                    description=event.description, 
                                    isDone=event.isDone,
                                    isCancelled=event.isCancelled,
                                    dayInMonth=event.dayInMonth,
                                    dayInWeek=event.dayInWeek,
                                    time=event.time)
        self.db.add(db_event)
        self.db.commit()
        self.db.refresh(db_event)
        return db_event
    
    def get_all(self):
        events = self.db.query(models.Product).all()
        return events
    
    def get_all_events_by_month(self):
        events = self.db.query(models.Event).all()
        events.sort(key=lambda event: event.dayInMonth)
        events_by_month = defaultdict(list)
        
        for event in events:
            event_month = event.dayInMonth 
            month_name = calendar.month_name[event_month]
            events_by_month[month_name].append(event)
        
        return events_by_month
        
    def remove(self, eventId: int):
        event = self.db.query(models.Event).filter(models.Event.id == eventId).first()
        self.db.delete(event)
        self.db.commit()
        return event
    
    def remove_by_month(self, eventsdayInMonth: int):
        events = self.db.query(models.Event).filter(models.Event.dayInMonth == eventsdayInMonth).all()
        for event in events:
            self.db.delete(event)
        self.db.commit()
        return events
    
    def update_all_event_atributtes(self,eventId: int, eventSchema: schema.Event):
        event = self.db.query(models.Event).filter(models.Event.id == eventId).first()
        event.name = eventSchema.name
        event.description = eventSchema.description
        event.isDone = eventSchema.isDone
        event.isCancelled = eventSchema.isCancelled
        event.dayInMonth = eventSchema.dayInMonth
        event.dayInWeek = eventSchema.dayInWeek
        event.time = eventSchema.time
        self.db.commit()
        self.db.refresh(event)
        return event
    
    def update_specific_event_atributtes(self, eventId: int, eventSchema: schema.EventSA):
        event = self.db.query(models.Event).filter(models.Event.id == eventId).first()
        event.name = eventSchema.name
        event.description = eventSchema.description
        event.dayInMonth = eventSchema.dayInMonth
        event.dayInWeek = eventSchema.dayInWeek
        event.time = eventSchema.time
        self.db.commit()
        self.db.refresh(event)  
        return event
    
    def update_is_done(self, eventId: int):
        event = self.db.query(models.Event).filter(models.Event.id == eventId).first()
        if event.isDone == False:
            event.isDone = True
        else:
            event.isDone = False
        self.db.commit()
        self.db.refresh(event)  
        return event
    
    def update_is_cancelled(self, eventId: int):
        event = self.db.query(models.Event).filter(models.Event.id == eventId).first()
        if event.isCancelled == False:
            event.isCancelled = True
        else:
            event.isCancelled = False 
            
        self.db.commit()
        self.db.refresh(event)  
        return event