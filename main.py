import telebot
from google import genai
from google.genai import types

BOT_TOKEN = "8910890961:AAEbfbSxJ8HbXMosOhRxB1f2C9BOJojEiqw"
GEMINI_KEY = "AQ.Ab8RN6KMx8aUYERZsZlg_-ThEuCBI6to1fCEyimJ83vh2kIQAg"

bot = telebot.TeleBot(BOT_TOKEN)
client = genai.Client(api_key=GEMINI_KEY)

@bot.message_handler(func=lambda message: True)
def chat_with_gemini(message):
    try:
        response = client.models.generate_content(
            model="gemini-4-argon",
            contents=message.text,
            config=types.GenerateContentConfig(
                thinking_config=types.ThinkingConfig(
                    thinking_level="high"
                )
            )
        )
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, f"Xatolik: {e}")

print("Argon High bot ishga tushdi...")
bot.polling(none_stop=True)