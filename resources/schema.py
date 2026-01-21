from pydantic import BaseModel, Field


class Resource(BaseModel):
    type: str = Field(..., min_length=1)
    status: str = Field(..., min_length=1)
    capacity: int


