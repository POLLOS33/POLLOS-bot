from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8875298341:AAHuul_eXSeLrzT7rWnzElJeApY8uAGwh3M"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bienvenue dans ta boutique 🛍️")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot lancé...")
    app.run_polling()

if __name__ == "__main__":
    main()




