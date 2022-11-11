from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from voice import text_to_voice
from pathlib import Path
import os
from get_weather import weather_info

# get your token from environment variables
TOKEN = os.getenv("TOKEN")

# get api_key
API = os.getenv("API_KEY")
# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"


# define a function for greeting with person
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, nice to meet you ")


# define a function which will receive some message from users and send back mirror message but in voice
async def receive_msg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_msg = update.message.text
    # return temperature and humidity values
    weather_data = weather_info(text_msg)

    if weather_data:
        # convert text into voice msg using text_to_voice function
        voice_msg = text_to_voice(f"Current weather temperature in  {text_msg} is  {weather_data[0]} degrees Celsius "
                                  f"and humidity about  {weather_data[1]} percent ")
        voice_path = Path("voice_data/")
        voice_file = voice_path / voice_msg
        file = open(f"{voice_file}", "rb")
        await context.bot.send_voice(chat_id=update.effective_chat.id, voice=file)
    else:
        voice_msg = text_to_voice("This is wrong city name or your location not found")
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


