import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from ensemble import ParaphraseEnsemble

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

class PlagiarismBot:
    def __init__(self):
        self.ensemble = ParaphraseEnsemble()

    def start(self, update: Update, context: CallbackContext):
        keyboard = [
            [InlineKeyboardButton("⚡ Fast Paraphrase", callback_data="fast")],
            [InlineKeyboardButton("✨ High Quality", callback_data="quality")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text(
            "🔍 *Plagiarism Remover Bot*\nChoose mode:",
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )

    def handle_choice(self, update: Update, context: CallbackContext):
        query = update.callback_query
        query.answer()
        choice = query.data
        context.user_data['mode'] = choice
        query.edit_message_text(f"✅ Mode: {'Fast ⚡' if choice == 'fast' else 'High Quality ✨'}\nSend text to paraphrase.")

    def paraphrase(self, update: Update, context: CallbackContext):
        mode = context.user_data.get('mode', 'fast')
        text = update.message.text
        
        try:
            if mode == "fast":
                result = self.ensemble.paraphrase_t5(text)
            else:
                result = self.ensemble.ensemble_paraphrase(text)
            
            update.message.reply_text(f"🔄 *Paraphrased Output:*\n\n{result}", parse_mode="Markdown")
        except Exception as e:
            logger.error(f"Error: {e}")
            update.message.reply_text("⚠️ Failed to process. Try shorter text or /start")

def main():
    TOKEN = os.getenv("TELEGRAM_TOKEN")
    PORT = int(os.environ.get("PORT", 8443))
    APP_NAME = os.environ.get("APP_NAME")

    bot = PlagiarismBot()
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", bot.start))
    dp.add_handler(CallbackQueryHandler(bot.handle_choice))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, bot.paraphrase))

    updater.start_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url=f"https://{APP_NAME}.herokuapp.com/{TOKEN}"
    )
    updater.idle()

if __name__ == "__main__":
    main()
