from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Todo(BaseModel):
    id: int
    author: str
    content: str
    timestamp: Optional[datetime] = None
