from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware

load_dotenv()

from fastapi import FastAPI
from auth.router import router as auth_router
from incidents.router import router as incident_router
from resources.router import router as resources_router
from websocket.routes import router as websocket_router
from core import logger_config


logger_config.setup_logging()




app = FastAPI(
    title="ResQLink",
    version="1.0.0"
)

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router)
app.include_router(incident_router)
app.include_router(resources_router)
app.include_router(websocket_router)