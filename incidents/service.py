from incidents.schemas import IncidentSchema, IncidentResourceSchema
from incidents.repository import insert_incident, insert_incident_resources, list_incidents

def create_incident(payload: IncidentSchema, user):
    user_data = {
        "type": payload.type,
        "severity": payload.severity,
        "description": payload.description,
        "location": payload.location,
        "status": payload.status,
        "created_by": user.id
    }

    return insert_incident(user_data)


def assign_resources(incident_id,payload: IncidentResourceSchema):
    assigned_incident = {
        "incident_id": incident_id,
        "resource_id": payload.resource_id,
    }
    return insert_incident_resources(assigned_incident)

def get_incidents(user):
    return list_incidents(user.id).data
