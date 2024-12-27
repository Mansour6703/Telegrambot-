from telebot import TeleBot

# اطلاعات ربات
BOT_TOKEN = '7732963099:AAFee9SbYp8vY5yZmXy_Dk1uBJxdQovns4'
CHAT_SOURCE = 'mohtavayenet'  # یوزرنیم کانال مبدا بدون @
CHAT_DEST = 'onlinecoffiinet'  # یوزرنیم کانال مقصد بدون @

bot = TeleBot(BOT_TOKEN)

# تابع دریافت پیام از کانال مبدا و ارسال به کانال مقصد
@bot.channel_post_handler()
def handle_new_post(message):
    if message.chat.username == CHAT_SOURCE:
        if message.text:
            bot.send_message(CHAT_DEST, message.text)
        elif message.photo:
            bot.send_photo(CHAT_DEST, message.photo[-1].file_id, caption=message.caption or "")

# اجرای ربات
bot.polling()

