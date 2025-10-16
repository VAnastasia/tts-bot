# Telegram Voice TTS Bot

Бот на Python для Telegram, который озвучивает присланные сообщения на русском языке с помощью ProxyAPI (OpenAI-совместимый endpoint, потоковый TTS).

## Возможности
- Принимает текстовые сообщения
- Генерирует голос (mp3) через ProxyAPI TTS (поддерживаются разные голоса)
- Отправляет результат в виде голосового сообщения
- Поддерживаются команды `/start` и `/help`
- Базовая обработка ошибок

## Быстрый старт

### 1. Клонируйте репозиторий и перейдите в папку

```sh
git clone <адрес-репозитория>
cd voice-bot
```

### 2. Установите зависимости

Рекомендуется использовать Python 3.9+ и venv:

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Получите необходимые ключи
- **TELEGRAM_TOKEN** — токен вашего Telegram-бота, выдается через [@BotFather](https://core.telegram.org/bots#botfather)
- **PROXY_API_KEY** — ваш ключ доступа к [ProxyAPI TTS](https://proxyapi.ru/docs/overview)

### 4. Создайте файл `.env` в корне проекта:

```
TELEGRAM_TOKEN=123456789:AAAbbbCCCdddEEEfff111222333xxxYYY
PROXY_API_KEY=your_proxyapi_key
```

### 5. Запустите бота

```sh
python telegram_tts_bot.py
```


## Использование
- Просто напишите боту текстовое сообщение — получите голосовое/аудио в ответ (mp3 через стримовое TTS ProxyAPI, голос "alloy" либо другой доступный).
- Команды:
  - `/start` — приветствие
  - `/help` — описание работы
- Поддерживается только текст, любые другие вложения игнорируются.

## Зависимости
- [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
- [openai (>=1.0)](https://pypi.org/project/openai/)
- [requests](https://pypi.org/project/requests/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## Примечания
- Для бота нужен стабильный интернет и доступ к https://api.proxyapi.ru/openai/v1
- Поддерживаемые голоса и параметры TTS смотрите в [документации ProxyAPI](https://proxyapi.ru/docs/overview).
- Если бот не запускается, проверьте формат .env и что ключи актуальны!

---

**Автор:** anastasiavasinskaa
