from fastapi import APIRouter, status
from fastapi.params import Depends
from auth.service import get_current_user
from notes.schema import Note
from notes import service
import logging


logger = logging.getLogger(__name__)

router = APIRouter(prefix="/notes", dependencies=[Depends(get_current_user)] ,tags=["notes"])


@router.post("/create-note/{incident_id}", status_code=status.HTTP_201_CREATED)
async def create_note(incident_id: str, payload:Note, user=Depends(get_current_user)):
    return await service.make_note(incident_id, payload, user)


@router.get("/get-notes/{incident_id}", status_code=status.HTTP_200_OK)
def get_notes(incident_id: str, user=Depends(get_current_user)):
    return  service.list_notes(incident_id)
