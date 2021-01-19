from datetime import datetime
from pydantic import BaseModel


class Post(BaseModel):
    id: int
    text: str
    created_date: datetime
    rubrics: str