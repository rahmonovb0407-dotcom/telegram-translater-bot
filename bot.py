import os
import telebot
from translate import Translator

TOKEN = os.environ.get("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)
tarjimon = Translator(to_lang="uz")

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👋 Salom! Menga matn yuboring.")

@bot.message_handler(func=lambda message: True)
def tarjima_qil(message):
    try:
        tarjima = tarjimon.translate(message.text)
        javob = f"Tarjima: {tarjima}"
        bot.reply_to(message, javob)
    except:
        bot.reply_to(message, "❌ Xato!")

print("🤖 Bot Railway da ishga tushdi...")
bot.polling()
