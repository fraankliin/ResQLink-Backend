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

def update_session_user(email):
    return (
        supabase
        .table('users')
        .update({
            "is_online": True,
            "is_available": True
        })
        .eq("email",email)


    )