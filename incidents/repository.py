from db.supabase import supabase


def insert_incident(incident: dict):
    return(
        supabase.
        table("incidents")
        .insert(incident)
        .execute()
    )


def insert_incident_resources(incident_resources: dict):
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

