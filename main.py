import telebot
from telebot import types

TOKEN = '5556384530:AAERLx8p3W4afDZgW6lKvWBGAOSvmef5h_U'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id, "Приветствуем в боте Anime Papercraft! \nВсегда рады видеть вас в нашей группе @papercraftanime")
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  item1 = types.KeyboardButton("Меню")
  markup.add(item1)
  bot.send_message(message.chat.id, 'Выбери раздел, которым бы ты хотел воспользоваться с помощью кнопок меню.\nТакже можно воспользоваться командой /menu \nПерезапустить бота /start', reply_markup=markup)


@bot.message_handler(content_types=["photo"])
def resend(message):
    bot.copy_message(chat_id="@papercraftcallback", from_chat_id=message.chat.id, message_id=message.id)
    bot.send_message("@papercraftcallback", "@" + str(message.chat.username))

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Ссылка на наш чатик 🥐")
    item2 = types.KeyboardButton("Назад")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, 'Отправлено!', reply_markup=markup)

    bot.send_message(message.chat.id, 'Присоединяйся к чатику, чтобы быть в курсе всех новостей и получать много годных развёрток от других ребят.', reply_markup=markup)

@bot.message_handler(commands=['menu'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Меню")
    markup.add(item1)
    bot.send_message(message.chat.id, 'Что тебя интересует?',reply_markup=markup)


@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == "Меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Отправить конкурсную работу 🏅️")
        item2 = types.KeyboardButton("Ссылка на наш чатик 🥐")
        item3 = types.KeyboardButton("Назад")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(message.chat.id, 'Что тебя интересует?', reply_markup=markup)
    elif message.text == "Отправить конкурсную работу 🏅️":
        bot.send_message(message.chat.id, 'Каждый может участвовать в конкурсе с одной работой на одного человека. Вышли снимки фигурки, соответствующие критериям, при желании можешь добавить подпись. Если остались вопросы по участию или выигрышу - можешь спросить в чате, нажав на кнопку с ссылкой на него.'

                                          '\n\n Учти, что ты можешь отправлять лишь самостоятельно собранные работы! Спасибо :3')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Назад")
        markup.add(item1)
        bot.send_message(message.chat.id, 'Отправь фото своей работы (и подпись к ней по желанию) :', reply_markup=markup)

    elif message.text == "Назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Меню")
        markup.add(item1)
        bot.send_message(message.chat.id, 'Возвращаемся в меню', reply_markup=markup)

    elif message.text == "Ссылка на наш чатик 🥐":
        bot.send_message(message.chat.id, "https://t.me/+zK8fBFGYtOU5Yjli")




bot.infinity_polling()