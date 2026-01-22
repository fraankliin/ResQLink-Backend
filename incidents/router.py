from fastapi import APIRouter, Depends, HTTPException, status
from auth.service import get_current_user
from incidents.schemas import IncidentSchema, IncidentResourceSchema, IncidentStatusUpdate
from incidents import service
import logging



logger = logging.getLogger(__name__)

router = APIRouter(prefix="/incidents", dependencies=[Depends(get_current_user)] ,tags=["incidents"])


@router.post("/create-incident", status_code=status.HTTP_201_CREATED)
def create_incident(payload: IncidentSchema ,user=Depends(get_current_user) ):
    return service.create_incident(payload, user)


@router.post("/incident-resources/{incident_id}", status_code=status.HTTP_200_OK)
async def create_incident_resources(incident_id:str, payload: IncidentResourceSchema ,user=Depends(get_current_user) ):
    return await service.assign_resources(incident_id,payload)


@router.get("/get-incidents", status_code=status.HTTP_200_OK)
def get_incidents(user=Depends(get_current_user)):
    return service.get_incidents(user)


@router.patch("/update-incident/{incident_id}", status_code=status.HTTP_200_OK)
async def update_incident_status(incident_id:str, payload:IncidentStatusUpdate, user=Depends(get_current_user) ):
    return await service.update_incident_status(incident_id,payload)



@router.patch("/assign/{incident_id}", status_code=status.HTTP_200_OK)
async def assign_incident(incident_id:str , payload: dict, user=Depends(get_current_user) ):
    return await service.assign_incident(incident_id,payload, user)



@router.get("/get-incident-by-rescuer", status_code=status.HTTP_200_OK)
def get_incidents(user=Depends(get_current_user)):
    return service.get_incident_by_rescuer(user.id)







