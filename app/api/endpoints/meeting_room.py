# app/api/meeting_room.py
from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import check_name_duplicate, check_meeting_room_exists
from app.core.db import get_async_session
from app.core.user import current_superuser
# Вместо импортов 6 функций импортируйте объект meeting_room_crud.
from app.crud.meeting_room import meeting_room_crud
from app.crud.reservation import reservation_crud
from app.schemas.meeting_room import (
    MeetingRoomCreate, MeetingRoomDB, MeetingRoomUpdate
)
from app.schemas.reservation import ReservationDB

router = APIRouter()


@router.post(
    '/',
    response_model=MeetingRoomDB,
    response_model_exclude_none=True,
    # Добавьте вызов зависимости при обработке запроса.
    dependencies=[Depends(current_superuser)],
)
async def create_new_meeting_room(

        meeting_room: MeetingRoomCreate,
        session: AsyncSession = Depends(get_async_session),
):
    """Только для суперюзеров."""
    await check_name_duplicate(meeting_room.name, session)
    # Замените вызов функции на вызов метода.
    new_room = await meeting_room_crud.create(meeting_room, session)
    return new_room


@router.get(
    '/{meeting_room_id}/reservations',
    response_model=list[ReservationDB],
    # Добавляем множество с полями, которые надо исключить из ответа.
    response_model_exclude={'user_id'},
)
async def get_reservations_for_room(
        meeting_room_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    await check_meeting_room_exists(meeting_room_id, session)
    reservations = await reservation_crud.get_future_reservations_for_room(
        room_id=meeting_room_id, session=session
    )
    return reservations


@router.patch(
    '/{meeting_room_id}',
    response_model=MeetingRoomDB,
    response_model_exclude_none=True,
    # Новая зависимость.
    dependencies=[Depends(current_superuser)],
)
async def partially_update_meeting_room(
        meeting_room_id: int,
        obj_in: MeetingRoomUpdate,
        session: AsyncSession = Depends(get_async_session),
):
    """Только для суперюзеров."""
    meeting_room = await check_meeting_room_exists(
        meeting_room_id, session
    )

    if obj_in.name is not None:
        await check_name_duplicate(obj_in.name, session)

    # Замените вызов функции на вызов метода.
    meeting_room = await meeting_room_crud.update(
        meeting_room, obj_in, session
    )
    return meeting_room


@router.delete(
    '/{meeting_room_id}',
    response_model=MeetingRoomDB,
    response_model_exclude_none=True,
    # Новая зависимость.
    dependencies=[Depends(current_superuser)],
)
async def remove_meeting_room(
        meeting_room_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    """Только для суперюзеров."""
    meeting_room = await check_meeting_room_exists(meeting_room_id, session)
    # Замените вызов функции на вызов метода.
    meeting_room = await meeting_room_crud.remove(meeting_room, session)
    return meeting_room
