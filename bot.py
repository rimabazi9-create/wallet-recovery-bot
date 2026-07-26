import os
import telebot
from telebot import types
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("TELEGRAM_TOKEN")

if not TOKEN:
    print("خطأ: يرجى التأكد من إضافة TELEGRAM_TOKEN في إعدادات البيئة على رندر.")
    exit(1)

bot = telebot.TeleBot(TOKEN)

try:
    bot.remove_webhook()
except Exception:
    pass

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item1 = types.KeyboardButton("🔐 استعادة محفظة رقمية")
    item2 = types.KeyboardButton("🔍 فحص عقد أو رابط")
    item3 = types.KeyboardButton("🛠 دعم فني وتدقيق")
    item4 = types.KeyboardButton("📞 التواصل مع الوسيط")
    markup.add(item1, item2, item3, item4)

    welcome_text = (
        "مرحباً بك في خدمة استعادة المحافظ والتدقيق المالي.\n\n"
        "الرجاء اختيار نوع الخدمة المطلوبة من القائمة أدناه، أو إرسال تفاصيل طلبك مباشرة:"
    )
    bot.reply_to(message, welcome_text, reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_request(message):
    user_name = message.from_user.first_name or "مستخدم"
    user_username = f"@{message.from_user.username}" if message.from_user.username else "بدون معرف"
    text = message.text

    acknowledgement = (
        "✅ تم استلام طلبك بنجاح.\n"
        "جاري تحويل تفاصيل الطلب إلى فريق الإدارة والوسيط المالي للمراجعة الفورية."
    )
    bot.reply_to(message, acknowledgement)

    print(f"[طلب جديد] من: {user_name} ({user_username}) | النص: {text}")

print("Bot is running perfectly...")
bot.infinity_polling(skip_pending=True)
