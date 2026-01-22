from db.supabase import supabase


async def insert_note(note:dict):
    return(
        supabase.
        table("incident_notes")
        .insert(note)
        .execute()
    )



def select_note(incident_id):
    return(
        supabase
        .table("incident_notes")
        .select("note", "created_at")
        .eq("incident_id", incident_id)
        .execute()
    )
