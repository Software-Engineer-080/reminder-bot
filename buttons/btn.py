import logging
from aiogram import Bot
from aiogram.types import BotCommand
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


logger = logging.getLogger(__name__)


# Функция создания реплай клавиатуры
async def buttons(buttons_lst: list, width: int = 3) -> ReplyKeyboardMarkup:

    """
    Создаёт текстовую клавиатуру кнопок

    Parameters
    ----------
    buttons_lst : list
        Список строковых значений под кнопки

    width : int
        Количество кнопок в строке

    Returns
    -------
    keyboard : ReplyKeyboardMarkup
        Текстовая клавиатура кнопок
    """

    repl_list = []

    for i in range(0, len(buttons_lst), width):

        lst = []

        for j in range(width):

            if i + j < len(buttons_lst):

                lst.append(KeyboardButton(text=buttons_lst[i + j]))

        repl_list.append(lst)

    keyboard = ReplyKeyboardMarkup(keyboard=repl_list, resize_keyboard=True)

    return keyboard


async def set_main_menu(bot: Bot):

    main_menu_commands = [

        BotCommand(command='/start',
                   description='Запуск бота')

    ]

    await bot.set_my_commands(main_menu_commands)
