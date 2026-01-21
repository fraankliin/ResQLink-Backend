from fastapi import APIRouter, Depends, HTTPException, status
from auth.service import get_current_user
from resources.schema import Resource
from resources import service
import logging



logger = logging.getLogger(__name__)

router = APIRouter(prefix="/resource", dependencies=[Depends(get_current_user)] ,tags=["resources"])


@router.post("/create-resource", status_code=status.HTTP_201_CREATED)
def create_resource(payload: Resource, user=Depends(get_current_user)):
    return service.create_source(payload, user)


@router.get("/get-resources", status_code=status.HTTP_200_OK)
def get_resources(user=Depends(get_current_user)):
    return service.get_resources(user)

