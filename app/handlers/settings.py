import json

from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from app.misc import get_settings, save_settings

import app.keyboards as kb

settings_router = Router()


class AutoEmoji(StatesGroup):
    emoji = State()


class AutoComment(StatesGroup):
    comment = State()


@settings_router.callback_query(F.data == "settings")
async def settings(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(
        f"⚙️Settings",
        reply_markup=kb.settings
    )


@settings_router.callback_query(F.data == "to_settings")
async def to_settings(callback: CallbackQuery, state: FSMContext):
    await callback.answer('')
    await state.clear()
    await callback.message.edit_text(
        f"⚙️Settings",
        reply_markup=kb.settings
    )


@settings_router.callback_query(F.data == "settings_emoji")
async def settings_emoji(callback: CallbackQuery, state: FSMContext):
    await state.set_state(AutoEmoji.emoji)
    await callback.answer('')

    settings = get_settings()

    await callback.message.edit_text(
        f"⚙️Settings > AutoEmoji\n\nCurrent:{settings['auto_reaction']}\n\nSend me emoji to set auto reaction!",
        reply_markup=kb.settings_emoji,
    )


@settings_router.message(AutoEmoji.emoji)
async def settings_emoji_2(message: Message, state: FSMContext):
    emoji = message.text
    await state.update_data(emoji=emoji)
    await state.clear()

    save_settings('auto_reaction', emoji)

    await message.answer(f"Auto reaction set to {emoji}")
    await message.answer(f"Settings", reply_markup=kb.settings)


@settings_router.callback_query(F.data == "settings_auto_comment")
async def settings_auto_comment(callback: CallbackQuery, state: FSMContext):
    await state.set_state(AutoComment.comment)
    await callback.answer('')

    settings = get_settings()

    await callback.message.edit_text(
        f"⚙️Settings > AutoEmoji\n\nCurrent:\n{settings['auto_comment']}\n\nSend me auto comment text!",
        reply_markup=kb.settings_first_message
    )


@settings_router.message(AutoComment.comment)
async def settings_auto_comment2(message: Message, state: FSMContext):
    comment = message.text
    await state.update_data(comment=comment)
    await state.clear()

    save_settings('auto_comment', comment)

    await message.answer(f"Auto comment:\n\n{comment}")
    await message.answer(f"Settings", reply_markup=kb.settings)
