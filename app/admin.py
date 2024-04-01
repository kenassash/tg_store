from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command, Filter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import app.keyboards as kb
from app.database.requests import get_users

admin = Router()

class Newsletter(StatesGroup):
    message = State()

class AdminProtect(Filter):
    async def __call__(self, message:Message):
        return message.from_user.id in [216159472]

@admin.message(AdminProtect(), Command('apanel'))
async def apanel(message: Message):
    await message.answer('Возможные команды /newletter')

@admin.message(AdminProtect(), Command('newletter'))
async def newsletter(message: Message, state: FSMContext):
    await state.set_state(Newsletter.message)
    await message.answer('Отправьте сообщение, которовые вы хотите разослать всем пользователям')

@admin.message(AdminProtect(), Newsletter.message)
async def newsletter_message(message: Message, state: FSMContext):
    await message.answer('Подождите .. идет рассылка')
    for user in await get_users():
        try:
            await message.send_copy(chat_id=user.tg_id)
        except:
            pass
    await message.answer('Рассылка успешно завершена')
    await state.clear()

    #46.39