from fastapi import APIRouter
from app.api.controller.webSocketController import router

api_router = APIRouter()
api_router.include_router(router, prefix="/websocket-entry", tags=["websockets"])
