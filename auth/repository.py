from db.supabase import supabase


def create_user(user: dict):
    return (
        supabase
        .table('users')
        .insert(user)
        .execute()
    )


def sign_up(email: str, password: str):
   return (
        supabase
        .auth
        .sign_up({
            "email": email,
            "password": password
        })
    )


def sign_in(email: str, password: str):
    return (
        supabase
        .auth
        .sign_in_with_password({
            "email": email,
            "password": password
        })
    )




def exists_by_email(email: str):
    response = (
        supabase
        .table("users")
        .select("id")
        .eq("email", email)
        .limit(1)
        .execute()
    )

    return len(response.data) > 0


def verify_jwt_token(token: str):
    return (
        supabase
        .auth
        .get_user(token)
    )

def update_session_user(user_id):
    return (
        supabase
        .table('users')
        .update({
            "is_online": True,
            "is_available": True
        })
        .eq("id",user_id)
        .execute()

    )

def logout_user(user_id):
    return (
        supabase
        .table('users')
        .update({
            "is_online": False,
            "is_available": False
        })
        .eq("id", user_id)
        .execute()

    )

def list_rescuers():
    return (
        supabase
        .table('users')
        .select("id", "name", "lastname", "email", "is_online", "is_available")
        .eq("role", "rescuer")
        .eq("is_online", True)
        .eq("is_available", True)
        .execute()
    )