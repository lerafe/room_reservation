# app/api/routers.py
from fastapi import APIRouter

from app.api.endpoints.meeting_room import router as meeting_room_router
from app.api.endpoints.reservation import router as reservation_router
from app.api.endpoints.user import router as user_router

main_router = APIRouter()
main_router.include_router(
    meeting_room_router, prefix='/meeting_rooms', tags=['Meeting Rooms']
)
main_router.include_router(
    reservation_router, prefix='/reservations', tags=['Reservations']
)
main_router.include_router(user_router)
