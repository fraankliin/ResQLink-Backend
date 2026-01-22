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


@router.post("/incident-resources/{incident_id}", status_code=status.HTTP_200_OK)
def create_incident_resources(incident_id:str, payload: IncidentResourceSchema ,user=Depends(get_current_user) ):
    return service.assign_resources(incident_id,payload)


@router.get("/get-incidents", status_code=status.HTTP_200_OK)
def get_incidents(user=Depends(get_current_user)):
    return service.get_incidents(user)




@router.patch("/assign/{incident_id}", status_code=status.HTTP_200_OK)
def assign_incident(incident_id:str , payload: dict, user=Depends(get_current_user) ):
    print(f"incident_id {incident_id}")
    return service.assign_incident(incident_id,payload)



@router.get("/get-incident-by-rescuer", status_code=status.HTTP_200_OK)
def get_incidents(user=Depends(get_current_user)):
    return service.get_incident_by_rescuer(user.id)







