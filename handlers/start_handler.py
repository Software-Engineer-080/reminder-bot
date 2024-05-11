# import asyncio
import logging
from storage import *
from filters import IsOwner
from aiogram import Router, Bot
from aiogram.types import Message
from buttons import inline_buttons
from setting import load_config, Config
from aiogram.filters import CommandStart
from aiogram.client.default import DefaultBotProperties


# --------------------------------- CONFIGURATION ---------------------------------


start_router = Router()

config: Config = load_config()

logger = logging.getLogger(__name__)

bot = Bot(token=config.tg_bot.token, default=DefaultBotProperties(parse_mode='HTML'))


# --------------------------------- STARTING ---------------------------------


@start_router.message(CommandStart(), IsOwner())
async def start_command(message: Message):
    await message.answer(text='Здравствуй, о Великий!\n\nЧем займёшься?',
                         reply_markup=await inline_buttons(buttons_lst=starting_btn))
