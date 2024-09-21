from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Кнопки после /start
ikb_start = InlineKeyboardMarkup(inline_keyboard=([
    [InlineKeyboardButton('Материалы с лекций', callback_data='materials_from_lectures')],
    [InlineKeyboardButton('Готовое ДЗ', callback_data='ready_made_dz')],
    [InlineKeyboardButton('Профиль', callback_data='profile')],
    [InlineKeyboardButton('Реферальная система', callback_data='referal_system')]
]))