from fastapi import APIRouter, Depends, HTTPException, status
from auth.schemas import UserCreate, UserLogin
from auth import service
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(payload: UserCreate):
    user = service.register(payload)
    return {"user": {
        "id": user.id,
        "email": user.email,
    }}



@router.post("/login", status_code=status.HTTP_200_OK)
def login_user(payload:UserLogin ):
    return service.login_supabase(payload)
