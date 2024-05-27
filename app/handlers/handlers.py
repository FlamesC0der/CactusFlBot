import json
import random

from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.types.reaction_type_emoji import ReactionTypeEmoji

from app.filters import IsAdmin
from app.misc import get_settings, get_emoji
import app.keyboards as kb

from app.handlers.settings import settings_router

router = Router()
router.include_router(settings_router)

emoji = get_emoji()
settings = get_settings()


@router.message(CommandStart(), IsAdmin(settings['admins_ids']))
async def cmd_start_admin(message: Message):
    await message.answer(f"Hi! {message.from_user.full_name}!\n\nYou have an admin access!", reply_markup=kb.main)


@router.callback_query(F.data == "to_main", IsAdmin(settings['admins_ids']))
async def cmd_start_admin2(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(f"Hi! {callback.from_user.full_name}!\n\nYou have an admin access!",
                                     reply_markup=kb.main)


@router.message(CommandStart(), ~IsAdmin(settings['admins_ids']))
async def cmd_start(message: Message):
    await message.answer(f"Hi! {message.from_user.full_name}\n\nIf you have any questions contact @FlamesCoder")


@router.message(Command(commands=emoji.keys()))
async def hug(message: Message):
    if message.reply_to_message:
        await message.reply_to_message.reply_sticker(random.choice(emoji[message.text[1:]]))
    else:
        await message.reply_sticker(random.choice(emoji[message.text[1:]]))


@router.channel_post()
async def channel_post(message: Message):
    settings = get_settings()
    await message.react([ReactionTypeEmoji(emoji=settings['auto_reaction'])])


@router.message(F.forward_origin.type == 'channel')  # AutoComment
async def channel_post(message: Message):
    settings = get_settings()
    await message.reply(settings['auto_comment'])
