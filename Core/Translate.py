import telebot
from googletrans import Translator
import os

API_TOKEN = os.environ.get("API_TOKENN")

bot = telebot.TeleBot(API_TOKEN)
translator = Translator()

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
     bot.reply_to(message,"سلام,من در حال حاظر میتونم فارسی رو به بقیه زبان هایی که میخواهی ترجمه کنم 😃")

@bot.message_handler(commands=['translate'])
def handle_translate(message):
    try:
        parts = message.text.split(maxsplit=2)
        if len(parts) < 3:
            bot.reply_to(message, "لطفاً زبان مقصد و متن را وارد کنید. مثلاً: /translate en سلام")
            return
        
        target_language = parts[1]
        text_to_translate = parts[2]
        
        translated = translator.translate(text_to_translate, dest=target_language)
        bot.reply_to(message, translated.text)
    except Exception as e:
        bot.reply_to(message, f"خطایی رخ داد: {e}")

bot.polling()








