from supabase import create_client
from core import config

supabase = create_client(
    config.SUPABASE_URL,
    config.SUPABASE_ROLE_KEY
)