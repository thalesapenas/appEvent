from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from src.infra.sqlalchemy.config.database import Base


class Event(Base):
    __tablename__= 'Events'
    
    id=Column(Integer, primary_key=True, index=True)
    name =Column(String) 
    description = Column(String)
    isDone = Column(Boolean)
    isCancelled = Column(Boolean)
    dayInMonth = Column(Integer)
    dayInWeek =  Column(Integer)
    time = Column(String)
    