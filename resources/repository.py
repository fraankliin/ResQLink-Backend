from db.supabase import supabase


def insert_resource(resource: dict):
    return(
        supabase.
        table("resources")
        .insert(resource)
        .execute()
    )


def list_resources(user_id):
    return(
        supabase.
        table("resources")
        .select("id", "type", "status", "capacity")
        .eq("created_by", user_id)
        .eq("status", "available")
        .execute()

    )