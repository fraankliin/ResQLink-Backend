from incidents.schemas import IncidentSchema, IncidentResourceSchema
from incidents.repository import insert_incident, insert_incident_resources, list_incidents, update_incident_assign, update_status_rescuer, list_incidents_rescuer


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


def assign_resources(incident_id, payload: IncidentResourceSchema):
    assigned_incident = {
        "incident_id": incident_id,
        "resource_id": payload.resource_id,
    }
    return insert_incident_resources(assigned_incident)


def get_incidents(user):
    return list_incidents(user.id).data



def assign_incident(incident_id, payload):
    update_status_rescuer(payload["rescuer_id"])
    return update_incident_assign(payload["rescuer_id"],incident_id )


def get_incident_by_rescuer(rescuer_id):
    return list_incidents_rescuer(rescuer_id).data
