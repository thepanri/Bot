import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "✅ Bot ngu đang chạy!")

print("🤖 Bot đang chạy...")
bot.infinity_polling()
 
