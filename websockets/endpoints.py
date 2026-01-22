from fastapi import APIRouter
from starlette.websockets import WebSocket, WebSocketDisconnect
from auth.service import get_current_user

router = APIRouter()

@router.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    token = ws.query_params.get("token")

    user = get_current_user()

    if not user:
        await ws.close(code=1008)
        return

    # await manager.connect(user.id, ws)
    #
    # try:
    #     while True:
    #         await ws.receive_text()
    # except WebSocketDisconnect:
    #     manager.disconnect(user.id)