from pydantic import BaseModel
from typing import Optional

# Base Model (Shared properties)
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


class TaskCreate(TaskBase):
    title: str
    description: str | None = None


class Task(TaskBase):
    id: int
    title: str
    description: str | None = None
    completed: bool = False

    class Config:
        from_attributes = True