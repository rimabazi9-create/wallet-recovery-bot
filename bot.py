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
    text = message.text
    
    if text == "🔐 استعادة محفظة رقمية":
        response = "يرجى تزويدي بنوع المحفظة (مثل Trust Wallet أو MetaMask) وآخر تاريخ كانت تعمل فيه للبدء بعملية الفحص واستعادة البيانات."
    elif text == "🔍 فحص عقد أو رابط":
        response = "يرجى إرسال الرابط أو العنوان المراد فحص والتحقق من سلامته عبر السيرفر."
    elif text == "🛠 دعم فني وتدقيق":
        response = "تم تسجيل طلب التدقيق الفني. سيتم مراجعة البيانات عبر الأدوات المتاحة."
    elif text == "📞 التواصل مع الوسيط":
        response = "سيتم تحويل طلبك للوسيط المالي المسؤول لمراجعة التفاصيل في أقرب وقت."
    else:
        response = f"تم استلام طلبك بنجاح:\n`{text}`\n\nجاري معالجة البيانات عبر السيرفر..."

    bot.reply_to(message, response, parse_mode="Markdown")

print("Bot with recovery menu is running...")
bot.infinity_polling(skip_pending=True)
