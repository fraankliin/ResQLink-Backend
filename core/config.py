from dotenv import load_dotenv
import os

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_ROLE_KEY= os.getenv("SUPABASE_SERVICE_ROLE_KEY")