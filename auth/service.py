from fastapi import HTTPException, status
from fastapi.params import Header
from supabase_auth.errors import AuthApiError

from auth.schemas import UserCreate, UserLogin
from auth.repository import create_user, sign_up, sign_in, verify_jwt_token, update_session_user
from core import security
import logging

logger = logging.getLogger(__name__)


def register(payload: UserCreate):

    try:
        result_signup = sign_up(payload.email, payload.password)
        if not result_signup.user:
            raise HTTPException(status_code=400, detail="No se pudo crear el usuario")

        user_data = {
            "id": result_signup.user.id,
            "name": payload.name,
            "lastname": payload.lastname,
            "email": payload.email,
            "role": payload.role,
        }
        create_user(user_data)
        return result_signup.user

    except AuthApiError as e:
        logger.error(f"Supabase Auth error: {e}")
        raise HTTPException(status_code=400, detail=f"Supabase error: {str(e)}")
    except Exception as e:
        logger.exception("Error inesperado al registrar usuario")
        raise HTTPException(status_code=500, detail="Error interno del servidor")

def login_supabase(payload: UserLogin):

    try:

        session = sign_in(payload.email, payload.password)

        if not session.session:
            raise HTTPException(status_code=401, detail="Email o contraseña incorrectos")

        update_session_user()

        return {
            "access_token": session.session.access_token,
            "refresh_token": session.session.refresh_token,
            "token_type": "bearer"
        }

    except AuthApiError as e:
        raise HTTPException(status_code=401, detail=f"Supabase error: {str(e)}")


def get_current_user(authorization: str = Header(...)):
    try:
        token = authorization.replace("Bearer ", "")
        res = verify_jwt_token(token)

        if not res or not res.user:
            raise Exception("No user")

        return res.user

    except Exception :
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )


# def get_rescue_available


