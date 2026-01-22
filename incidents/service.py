from incidents.schemas import IncidentSchema, IncidentResourceSchema, IncidentStatusUpdate
from incidents.repository import insert_incident, insert_incident_resources, list_incidents, update_incident_assign, \
    update_status_rescuer, list_incidents_rescuer, update_status
from websocket.events import RESCUER_ASSIGNED, INCIDENT_STATUS_UPDATED, RESOURCES_ASSIGNED
from websocket.manager import manager


def create_incident(payload: IncidentSchema, user):
    user_data = {
        "type": payload.type,
        "severity": payload.severity,
        "description": payload.description,
        "city": payload.city,
        "address": payload.address,
        "status": payload.status,
        "created_by": user.id
    }

    return insert_incident(user_data)


async def assign_resources(incident_id, payload: IncidentResourceSchema):
    assigned_incident = {
        "incident_id": incident_id,
        "resource_id": payload.resource_id,
    }

    await insert_incident_resources(assigned_incident)

    await manager.emit_to_incident(
        incident_id,
        {
            "event": RESOURCES_ASSIGNED,
            "incident_id": incident_id,
            "data": {
                "resource_id": payload.resource_id,
            }
        }
    )

    return {"resource_assigned": payload.resource_id}


def get_incidents(user):
    return list_incidents(user.id).data


async def assign_incident(incident_id, payload, operator):
    await update_status_rescuer(payload["rescuer_id"])
    await update_incident_assign(payload["rescuer_id"], incident_id)

    await manager.subscribe(incident_id, operator.id)
    await manager.subscribe(incident_id, payload["rescuer_id"])

    await manager.emit_to_incident(
        incident_id,
        {
            "event": RESCUER_ASSIGNED,
            "incident_id": incident_id,
            "data": {
                "rescuer_id": payload["rescuer_id"],
                "status": "asignado",

            }
        }
    )

    return {"assigning_to": payload["rescuer_id"]}


def get_incident_by_rescuer(rescuer_id):
    return list_incidents_rescuer(rescuer_id).data


async def update_incident_status(incident_id, payload: IncidentStatusUpdate):
    await update_status(incident_id, payload.status)

    await manager.emit_to_incident(
        incident_id,
        {
            "event": INCIDENT_STATUS_UPDATED,
            "incident_id": incident_id,
            "data": {
                "new_status": payload.status,
            }
        }
    )

    return {"incident_status": payload.status}
