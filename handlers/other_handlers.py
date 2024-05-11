# import asyncio
import logging
from storage import *
from filters import IsOwner
from aiogram import Router, Bot, F
from buttons import inline_buttons
from setting import load_config, Config
from aiogram.types import CallbackQuery
from aiogram.client.default import DefaultBotProperties


# --------------------------------- CONFIGURATION ---------------------------------


other_router = Router()

config: Config = load_config()

logger = logging.getLogger(__name__)

bot = Bot(token=config.tg_bot.token, default=DefaultBotProperties(parse_mode='HTML'))


# --------------------------------- OTHERS ---------------------------------


@other_router.callback_query(F.data.in_(can_dict), IsOwner())
async def start_command(callback: CallbackQuery):
    await callback.message.edit_text(text=quest_can_you, reply_markup=await inline_buttons(buttons_lst=program_btn,
                                                                                           buttons_per_row=1))
