import os
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("TELEGRAM_TOKEN")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def start(update: Update, context: CallbackContext):
    update.message.reply_text("أهلاً بك! بوت استعادة المحافظ والتحقق من المعاملات يعمل بنجاح وجاهز لخدمتكم.")

def handle_message(update: Update, context: CallbackContext):
    text = update.message.text
    update.message.reply_text(f"تم استلام طلبك أو رابط المعاملة بنجاح:\n{text}\n\nجاري فحص البيانات عبر السيرفر...")

def main():
    if not TOKEN:
        print("خطأ: يرجى التأكد من إضافة TELEGRAM_TOKEN في إعدادات البيئة على رندر.")
        return

    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), handle_message))

    print("Telegram Bot is starting and listening for customers...")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
