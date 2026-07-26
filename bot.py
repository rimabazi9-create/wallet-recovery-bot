import os
import telebot
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("TELEGRAM_TOKEN")

if not TOKEN:
    print("خطأ: يرجى التأكد من إضافة TELEGRAM_TOKEN في إعدادات البيئة على رندر.")
    exit(1)

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! بوت استعادة المحافظ والتحقق من المعاملات يعمل بنجاح وجاهز لخدمتكم.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    text = message.text
    bot.reply_to(message, f"تم استلام طلبك أو رابط المعاملة بنجاح:\n{text}\n\nجاري فحص البيانات عبر السيرفر...")

print("Telegram Bot is starting and listening for customers...")
bot.infinity_polling()
