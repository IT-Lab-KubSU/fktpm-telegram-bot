from typing import NoReturn, List
from aiogram import Router

from handlers.user.routes.chat_routes import chat_router

routers: List[Router] = [chat_router]


def register_handlers(main_router: Router) -> NoReturn:
    for router in routers:
        main_router.include_router(router)