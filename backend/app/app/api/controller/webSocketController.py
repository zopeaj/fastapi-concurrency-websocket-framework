from fastapi import APIRouter, WebSocket
from fastapi.responses import HTMLResponse

router = APIRouter()

html = ""

async def get_cookie_or_token(websocket: WebSocket, session: Optional[str] = Cookie(None), token: Optional[str] = Query(None),):
    if session is None and token is None:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
    return session or token

@router.get("/")
async def get():
    return HTMLResponse(html)

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")

@router.websocket("/items/{item_id}/ws")
async def websocket_endpoint(websocket: WebSocket, item_id: str, q: Optional[str] = None, cookie_or_token: str = Depends(get_cookie_or_token),):
    await websocket.accept()
    while True:
    data = await websocket.receive_text()
    await websocket.send_text(f"Session cookie or query token value is: {cookie_or_token}")
    if q is not None:
        await websocket.send_text(f"Query paramter q is: {q}")
    await websocket.send_text(f"Message text was: {data}, for item ID: {item_id}")
