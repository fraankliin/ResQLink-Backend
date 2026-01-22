from pydantic import BaseModel, Field


class IncidentSchema(BaseModel):
    type: str = Field(..., min_length=1)
    severity: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)
    city: str = Field(..., min_length=1)
    address: str = Field(..., min_length=1)
    status: str = Field(..., min_length=1)

class IncidentResourceSchema(BaseModel):
    resource_id: str = Field(..., min_length=1)


class IncidentStatusUpdate(BaseModel):
    status: str = Field(..., min_length=1)