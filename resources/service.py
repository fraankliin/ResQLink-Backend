from resources import repository
from resources.schema import Resource




def create_source(payload: Resource, user):
    source_data = {
        "type": payload.type,
        "status": payload.status,
        "created_by": user.id   ,
        "capacity": payload.capacity,
        }




    return repository.insert_resource(source_data)




def get_resources(user):
    return repository.list_resources(user.id).data



def get_resources_by_incident(incident_id):
    return repository.list_resources_by_incident(incident_id)




