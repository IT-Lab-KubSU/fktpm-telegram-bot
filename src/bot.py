from typing import NoReturn
from pathlib import Path
from loguru import logger
from asyncio import run

from aiogram import Dispatcher, Bot
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import register_handlers


async def main() -> NoReturn:
    base_dir = Path(__file__).resolve().parent.parent

    logger.add(base_dir / 'logs.log', level='INFO')

    import config

    dp: Dispatcher = Dispatcher(storage=MemoryStorage())
    bot = Bot(config.BOT_TOKEN)
    register_handlers(dp)

    logger.info('Bot started')
    await dp.start_polling(bot)
    logger.info('Bot stopped')


if __name__ == '__main__':
    run(main())


