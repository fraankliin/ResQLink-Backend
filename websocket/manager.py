from typing import Dict, Set
from fastapi import WebSocket
import logging

logger = logging.getLogger(__name__)

class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}
        self.incident_rooms: Dict[str, Set[str]] = {}

    async def connect(self, user_id: str, ws: WebSocket):
        await ws.accept()
        self.active_connections[user_id] = ws

    def disconnect(self, user_id: str):
        self.active_connections.pop(user_id, None)
        for users in self.incident_rooms.values():
            users.discard(user_id)

    async def subscribe(self, incident_id: str, user_id: str):
        self.incident_rooms.setdefault(incident_id, set()).add(user_id)
        logger.info(f"[WS] user={user_id} subscribed to incident={incident_id}")


    async def emit_to_incident(self, incident_id: str, payload: dict):
        users = self.incident_rooms.get(incident_id, set())
        logger.info(f"[WS] emitting {payload['event']} to incident={incident_id} users={users}")
        for user_id in self.incident_rooms.get(incident_id, set()):
            ws = self.active_connections.get(user_id)
            if ws:
                await ws.send_json(payload)

manager = ConnectionManager()
