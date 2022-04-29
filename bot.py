import logging
from aiogram import Bot, Dispatcher, executor, types

import config

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['start', 'help'])
async def send_help(message: types.Message):
    await message.reply("Чат-бот для гимназии 174.\n(Пока что в разработке)")


@dp.message_handler(lambda message: message.text == 'Поступление')
async def send_class(message: types.Message):
    button_class5 = types.InlineKeyboardButton('5 класс', callback_data='entrance_class5')
    button_class10 = types.InlineKeyboardButton('10 класс', callback_data='entrance_class10')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(button_class5, button_class10)

    await message.answer('Выберите класс', reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data.startswith('entrance'))
async def process_callback_button1(callback: types.CallbackQuery):
    if callback.data.endswith('class5'):
        await bot.send_message(callback.from_user.id, config.entrance_class5)
    elif callback.data.endswith('class10'):
        await bot.send_message(callback.from_user.id, config.entrance_class10)


@dp.message_handler(lambda message: message.text == 'Связь с директором')
async def send_class(message: types.Message):
    await message.answer(config.call_director)


@dp.message_handler(content_types=['text'])
async def entrance(message: types.Message):
    button_entrance = types.KeyboardButton('Поступление')
    button_call_director = types.KeyboardButton('Связь с директором')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(button_entrance, button_call_director)

    await message.answer(message.text, reply_markup=keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
