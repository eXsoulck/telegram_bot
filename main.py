from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from voice import text_to_voice
from pathlib import Path
import os


# get your token from environment variables
TOKEN = os.getenv("TOKEN")


# define a function for greeting with person
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, nice to meet you ")


# define a function which will receive some message from users and send back mirror message but in voice
async def receive_msg(update: Update,context: ContextTypes.DEFAULT_TYPE):
    text_msg = update.message.text
    # convert text into voice msg using text_to_voice function
    voice_msg = text_to_voice(text_msg)
    voice_path = Path("voice_data/")
    voice_file = voice_path / voice_msg
    file = open(f"{voice_file}", "rb")
    await context.bot.send_voice(chat_id=update.effective_chat.id, voice=file)



if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler('start', start)
    msg_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, receive_msg)

    application.add_handler(start_handler)
    application.add_handler(msg_handler)

    application.run_polling()
