import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv

load_dotenv()

# قراءة التوكن من متغيرات البيئة في رندر
TOKEN = os.environ.get("TELEGRAM_TOKEN")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً بك! بوت استعادة المحافظ والتحقق من المعاملات يعمل بنجاح وجاهز لخدمتكم.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    # يمكنك إضافة منطق الفحص أو الرد على الزبائن هنا
    await update.message.reply_text(f"تم استلام طلبك أو رابط المعاملة بنجاح:\n{text}\n\nجاري فحص البيانات عبر السيرفر...")

def main():
    if not TOKEN:
        print("خطأ: يرجى التأكد من إضافة TELEGRAM_TOKEN في إعدادات البيئة على رندر.")
        return

    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    print("Telegram Bot is starting and listening for customers...")
    application.run_polling()

if __name__ == '__main__':
    main()
