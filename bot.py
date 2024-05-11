import asyncio
import logging
from datetime import datetime
from buttons import set_main_menu
from aiogram import Bot, Dispatcher
from setting import Config, load_config
from handlers import start_router, other_router
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties

from storage import owner

logger = logging.getLogger(__name__)

config: Config = load_config()

bot = Bot(token=config.tg_bot.token, default=DefaultBotProperties(parse_mode='HTML'))


async def dev() -> None:

    while True:
        await asyncio.sleep(1)

        current_time = datetime.now().time()

        if current_time.hour == 20 and current_time.minute == 00:
            message = await bot.send_message(chat_id=owner, text='🔥 Займись программированием! 🔥')

            if message.message_id - 1:
                await bot.delete_message(chat_id=owner, message_id=message.message_id - 1)

            await asyncio.sleep(60 * 60 * 24)


async def main() -> None:
    logging.basicConfig(
        level=logging.DEBUG,
        format='#{levelname:8} [{asctime}] {filename:14}: {lineno:4} - {name:18} - {message}',
        style='{'
    )

    logger.info('Starting bot')

    dp = Dispatcher(storage=MemoryStorage())

    await set_main_menu(bot)

    dp.include_router(start_router)
    dp.include_router(other_router)

    await bot.delete_webhook(drop_pending_updates=True)

    tasks = [
        dev(),
        dp.start_polling(bot, polling_timeout=5)
    ]

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
