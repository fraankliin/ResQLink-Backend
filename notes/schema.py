from pydantic import BaseModel, Field


class Note(BaseModel):
    note: str = Field(..., min_length=1)
