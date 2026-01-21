from typing import Literal

from pydantic import BaseModel, field_validator, EmailStr, Field


class UserResponse(BaseModel):
    email: EmailStr

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserCreate(BaseModel):
    name: str = Field(..., min_length=1)
    lastname: str = Field(..., min_length=1)
    email: EmailStr = Field(..., min_length=1)
    password: str = Field(..., min_length=8)
    role: Literal["operator", "rescuer"]


    @field_validator("email")
    @classmethod
    def normalize_email(cls, v):
        return v.lower().strip()

    @field_validator("name")
    @classmethod
    def normalize_name(cls, v):
        return v.lower().strip()

    @field_validator("lastname")
    @classmethod
    def normalize_lastname(cls, v):
        return v.lower().strip()


