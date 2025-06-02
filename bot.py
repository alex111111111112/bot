from telegram import Bot, Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import Updater, CommandHandler, CallbackContext

# Твой токен бота
import os
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Функция, которая будет отправлять кнопку
def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(
            text="🚀 Открыть мини-апп Olkhon Full Gid",
            web_app=WebAppInfo(url="https://olkhon.ucoz.net/index.html")
        )]
    ])
    context.bot.send_message(
        chat_id=chat_id,
        text="Привет! Нажми кнопку ниже, чтобы открыть мини-апп:",
        reply_markup=keyboard
    )

# Настройка бота
updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler("start", start))

# Запуск
updater.start_polling()
updater.idle()
