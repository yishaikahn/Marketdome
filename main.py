from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# --- תפריט ראשי ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔔 הפעל/כבה התראות", callback_data='toggle_alerts')],
        [InlineKeyboardButton("⏱ שנה תדירות", callback_data='change_interval')],
        [InlineKeyboardButton("📈 הוסף מניה", callback_data='add_stock')],
        [InlineKeyboardButton("💰 הוסף מטבע", callback_data='add_crypto')],
        [InlineKeyboardButton("🧹 נקה רשימות", callback_data='clear_lists')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("🎛 תפריט שליטה:", reply_markup=reply_markup)

# --- תגובות לתפריט ---
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'toggle_alerts':
        # פעולה להפעיל/לכבות התראות
        await query.edit_message_text("🔔 התראות הוחלפו (לא באמת, עדיין בתהליך בנייה)")
    elif query.data == 'change_interval':
        await query.edit_message_text("בחר תדירות:", reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("⏱ כל 5 דקות", callback_data='interval_5')],
            [InlineKeyboardButton("⏱ כל 15 דקות", callback_data='interval_15')],
            [InlineKeyboardButton("⏱ כל 30 דקות", callback_data='interval_30')],
            [InlineKeyboardButton("⏱ כל 60 דקות", callback_data='interval_60')],
        ]))
    elif query.data.startswith("interval_"):
        minutes = query.data.split("_")[1]
        await query.edit_message_text(f"⏱ תדירות שונתה ל-{minutes} דקות")
        # פה תעדכן config.json
    elif query.data == 'add_stock':
        await query.edit_message_text("שלח לי את הסימול של המניה שתרצה להוסיף.")
        # מצב 'המתנה לקלט'
    elif query.data == 'add_crypto':
        await query.edit_message_text("שלח לי את שם המטבע (למשל: bitcoin).")
    elif query.data == 'clear_lists':
        await query.edit_message_text("📤 הרשימות נוקו (תיאורטית).")

# --- הפעלה ---
def run_bot():
    app = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()

if __name__ == "__main__":
    run_bot()
    