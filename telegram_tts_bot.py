import asyncio
from openai import AsyncOpenAI
import telebot
import os
from dotenv import load_dotenv  # загрузка .env

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
OPENAI_PROXYAPI_KEY = os.getenv('PROXY_API_KEY')

bot = telebot.TeleBot(TELEGRAM_TOKEN)

HELP_MESSAGE = (
    'Этот бот озвучивает ваши текстовые сообщения с помощью ProxyAPI TTS (OpenAI совместимый эндпоинт).\n'
    'Просто пришлите текст, и получите голосовое сообщение!\n'
    '\nДоступные команды:\n'
    '/start – приветствие\n'
    '/help – информация о боте'
)

openai = AsyncOpenAI(
    api_key=OPENAI_PROXYAPI_KEY,
    base_url="https://api.proxyapi.ru/openai/v1"
)

async def synthesize_tts_async(text: str) -> bytes:
    async with openai.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="alloy",
        input=text,
        instructions="Говори чётко, эмоционально и натурально. На русском языке. Без акцентов.",
        response_format="mp3",
    ) as response:
        return await response.read()  # исправлено: read вместо aread

# Синхронная обёртка для telebot
def synthesize_tts(text: str) -> bytes:
    return asyncio.run(synthesize_tts_async(text))

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет! Пришли мне сообщение, и я озвучу его :)\nДля справки напиши /help')

@bot.message_handler(commands=['help'])
def help_handler(message):
    bot.send_message(message.chat.id, HELP_MESSAGE)

@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.strip()
    if not text:
        bot.reply_to(message, 'Ошибка: Пустое сообщение!')
        return
    try:
        audio_bytes = synthesize_tts(text)
        bot.send_voice(message.chat.id, audio_bytes, reply_to_message_id=message.message_id)
    except Exception as e:
        bot.reply_to(message, f'Ошибка при синтезе речи: {e}')

@bot.message_handler(content_types=["audio", "voice", "photo", "video", "sticker"])
def unsupported_handler(message):
    bot.send_message(message.chat.id, 'Пожалуйста, отправьте только текстовое сообщение для озвучивания.')

if __name__ == '__main__':
    print('Бот запущен...')
    bot.infinity_polling()
