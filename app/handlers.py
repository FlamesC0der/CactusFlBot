import os
import json
import random

from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.types.reaction_type_emoji import ReactionTypeEmoji

router = Router()

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets/emoji.json')) as f:
    EMOJI = json.load(f)


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Hi! If you have any questions contact @FlamesCoder")


@router.message(Command(commands=EMOJI.keys()))
async def hug(message: Message):
    if message.reply_to_message:
        await message.reply_to_message.reply_sticker(random.choice(EMOJI[message.text[1:]]))
    else:
        await message.reply_sticker(random.choice(EMOJI[message.text[1:]]))


@router.channel_post()
@router.edited_channel_post()
async def channel_post(message: Message):
    await message.react([ReactionTypeEmoji(emoji='💘')])


@router.message(F.forward_origin.type == 'channel')  # AutoComment
async def channel_post(message: Message):
    await message.reply('Это первое сообщение эшкереее!\nЛинка милашка💘Люлбю💘\nМилка дура кста)')
