from fastapi import APIRouter

from app.hyuabot.api.core.fetch.bus import fetch_bus_router
from app.hyuabot.api.core.fetch.food import fetch_restaurant_menu_router
from app.hyuabot.api.core.fetch.reading_room import fetch_reading_room_router
from app.hyuabot.api.core.fetch.subway import fetch_subway_router

fetch_router = APIRouter(prefix="/fetch")
fetch_router.include_router(fetch_bus_router)
fetch_router.include_router(fetch_reading_room_router)
fetch_router.include_router(fetch_restaurant_menu_router)
fetch_router.include_router(fetch_subway_router)
