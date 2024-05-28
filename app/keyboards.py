from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⚙️Settings", callback_data="settings")]
])

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="AutoEmoji", callback_data="settings_emoji")],
    [InlineKeyboardButton(text="AutoComment", callback_data="settings_auto_comment")],
    [InlineKeyboardButton(text="Back", callback_data="to_main")]
])

settings_emoji = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Back", callback_data="to_settings")]
])

settings_first_message = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Back", callback_data="to_settings")]
])
