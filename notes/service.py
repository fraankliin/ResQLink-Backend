from notes.schema import Note
from notes.repository import insert_note, select_note
from websocket.manager import manager
from websocket.events import FIELD_NOTE_ADDED


async def make_note(incident_id , payload:Note, user):
    data_note = {
        "incident_id": incident_id,
        "author_id": user.id,
        "note": payload.note,
    }

    await manager.emit_to_incident(
        incident_id,
        {
            "event": FIELD_NOTE_ADDED,
            "incident_id": incident_id,
            "data": {
                "resource_id": payload.note,
            }
        }
    )


    await insert_note(data_note)


    return {"note": payload.note}


def list_notes(incident_id):
    return select_note(incident_id).data

