from fastapi import APIRouter, Depends, HTTPException, status
from auth.service import get_current_user
from incidents.schemas import IncidentSchema, IncidentResourceSchema
from incidents import service
import logging



logger = logging.getLogger(__name__)

router = APIRouter(prefix="/incidents", dependencies=[Depends(get_current_user)] ,tags=["incidents"])


@router.post("/create-incident", status_code=status.HTTP_201_CREATED)
def create_incident(payload: IncidentSchema ,user=Depends(get_current_user) ):
    return service.create_incident(payload, user)


@router.get("/get-inci", status_code=status.HTTP_200_OK)
def get_resources(user=Depends(get_current_user)):
    return service.get_resources(user)


@router.post("/incident-resources/{incident_id}", status_code=status.HTTP_200_OK)
def create_incident_resources(incident_id:str, payload: IncidentResourceSchema ,user=Depends(get_current_user) ):
    return service.assign_resources(incident_id,payload)


@router.get("/get-incidents", status_code=status.HTTP_200_OK)
def get_incidents(user=Depends(get_current_user)):
    return service.get_incidents(user)




# @router.patch("/assign", status_code=status.HTTP_200_OK)
# def assign_incident(payload: IncidentResourceSchema ,user=Depends(get_current_user) ):
#







