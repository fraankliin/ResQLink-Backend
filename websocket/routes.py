from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from auth.service import get_current_user
from websocket.manager import manager
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

@router.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    token = ws.query_params.get("token")
    user = await get_current_user(token)

    if not user:
        await ws.close(code=1008)
        return

    await manager.connect(user.id, ws)

    try:
        while True:
            logger.info("Conexion WS establecida correctamente")
            await ws.receive_json()  # (opcional para futuros comandos)
    except WebSocketDisconnect:
        manager.disconnect(user.id)
