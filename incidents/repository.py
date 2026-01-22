from db.supabase import supabase


def insert_incident(incident: dict):
    return(
        supabase.
        table("incidents")
        .insert(incident)
        .execute()
    )


async def insert_incident_resources(incident_resources: dict):
    return(
        supabase
        .table("incident_resources")
        .insert(incident_resources)
        .execute()
    )


def list_incidents(user_id):
    return(
        supabase.
        table("incidents")
        .select()
        .eq("created_by", user_id)
        .execute()

    )

async def update_incident_assign(rescuer_id, incident_id):
    return(
        supabase
        .table("incidents")
        .update({"assigned_to": rescuer_id,
                 "status": "asignado"})
        .eq("id", incident_id)
        .execute()
    )


async def update_status_rescuer(rescuer_id):
    return (
        supabase
        .table('users')
        .update({
            "is_available": False
        })
        .eq("id", rescuer_id)
        .execute()

    )


def list_incidents_rescuer(rescuer_id):
    return(
        supabase
        .table("incidents")
        .select()
        .eq("assigned_to", rescuer_id)
        .execute()
    )


async def update_status(incident_id, status):
    return(
        supabase
        .table("incidents")
        .update({"status": status})
        .eq("id", incident_id)
        .execute()
    )