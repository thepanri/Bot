import telebot
import os

TOKEN = os.getenv("7961535921:AAEJFrNuBSzC0Win1gMPIYicIxAVmCINB74")  # Lấy token từ biến môi trường

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "✅ Bot đang chạy trên Render!")

print("🤖 Bot đang chạy...")
bot.infinity_polling()
 
