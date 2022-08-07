import telebot


TOKEN = '5556384530:AAERLx8p3W4afDZgW6lKvWBGAOSvmef5h_U'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=["photo", 'sticker'])
def resend(message):
    bot.copy_message(chat_id="@papercraftcallback", from_chat_id=message.chat.id, message_id=message.id)


bot.polling()