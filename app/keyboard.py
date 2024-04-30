from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='/start')],
    [KeyboardButton(text='/help')]
], resize_keyboard=True, input_field_placeholder='Выберите нужную операцию.')
