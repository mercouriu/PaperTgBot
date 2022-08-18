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
        item2 = types.KeyboardButton("Правила конкурса 📄")
        item3 = types.KeyboardButton("Ссылка на наш чатик 🥐")
        item4 = types.KeyboardButton("Назад")

        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        bot.send_message(message.chat.id, 'Что тебя интересует?', reply_markup=markup)
    elif message.text == "Отправить конкурсную работу 🏅️":
        bot.send_message(message.chat.id, 'Каждый может участвовать в конкурсах. Вышли фото фигурки, соответствующие критериям (их ты можешь прочитать в закрепе чата или нажав на соответствующую кнопку), при желании можешь добавить подпись к картинкам с именем или тайтлом фигурки. Если остались вопросы по участию или выигрышу - можешь спросить в чате, нажав на кнопку с ссылкой на него.'

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

    elif message.text == "Правила конкурса 📄":
        bot.send_message(message.chat.id, "1. Информация по конкурсу"
                                          "\n1.1 В первом конкурсе Вам нужно собрать фигурку с нуля или доделать незаконченную"
                                          "\n1.1.1 Для участия Вам просто нужно отправить фотографии в бота @AnimePapercraftBot до дедлайна"
                                          "\n1.1.2 Отправляются следующие фотографии: в процессе сборки с листочком, подписанным Конкурс 1; готовая фигурка напротив источника света или окна, если сделано из тонкой бумаги (чтобы были видны внутренние крылышки и швы); фото готовой фигурки без надписей (анфас или 3/4, для оценки). Редактировать фотки нельзя, разве что играться со светом и цветокоррекцией."
                                          "\n1.2 Во втором конкурсе Вам нужно красиво сфотографировать любую уже собранную фигурку"
                                          "\n1.2.1 Для участия Вам просто нужно отправить фотографии в бота @AnimePapercraftBot до дедлайна"
                                          "\n1.2.2 Вам нужно прислать необработанную фотографию собранной фигурки с сигной Конкурс 2 и саму конкурсную фотку. Принимаются любые фотографии, любой фон, любой ракурс. Допускается обработка фотографии, как световая/цветовая, так и небольшая эстетическая обработка швов, печати (только не переусердствовать, должно быть понятно, что фигурка бумажная)"
                                          "\n\n2. Правила проведения"
                                          "\n2.1 Участвовать можно в двух конкурсах сразу и с любым количеством работ на человека. Пожалуйста, не отправляйте фотографии сразу на два конкурса или несколько заходов на один конкурс, лучше разделите вложения."
                                          "\n2.2  Отправлять работы можно до двадцатого сентября (20.09.2022) включительно"
                                          "\n2.3 Места будут определяться путем голосования участников с 21.09 до 29.09 включительно")





bot.infinity_polling()