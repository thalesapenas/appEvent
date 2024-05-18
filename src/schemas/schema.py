from pydantic import BaseModel
from typing import List, Optional, ForwardRef


class Event (BaseModel):
    id : Optional[int]  = None
    name: Optional[str] = f"event{id}"
    description : str
    isDone : bool = False
    isCancelled : bool = False
    dayInMonth : int
    dayInWeek : int
    time : str
    
class EventSA(BaseModel): #Event Specific Atributtes   
    name: Optional[str] = None
    description : Optional[str] = None
    dayInMonth : Optional[int] = None
    dayInWeek : Optional[int] = None
    time : Optional[str] = None


    