from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

TOKEN = "7604995802:AAEDqUkdXFc59u4a5GmlauqD_rdUoTTE9e4"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📊 קבל התראה", callback_data='alert')],
        [InlineKeyboardButton("💡 מצא הזדמנות", callback_data='opportunity')],
        [InlineKeyboardButton("⏱ שנה תדירות", callback_data='frequency')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "ברוך הבא ל־MarketDome – הבוט שמתריע על תנועות חזקות בשוק 📈\nבחר פעולה:",
        reply_markup=reply_markup
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "alert":
        await query.edit_message_text("🚨 ביטקוין ירד ב־8%. השוק מגיב בעצבנות.")
    elif query.data == "opportunity":
        await query.edit_message_text("💡 הזדמנות: דירת 3 חדרים בגילה – 1.75 מיליון ש״ח. מציאה!")
    elif query.data == "frequency":
        await query.edit_message_text("⏱ התדירות עודכנה לפעם ביום. (דמו)")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

app.run_polling()