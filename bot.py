from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram.error import NetworkError
import logging

# Включаем логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Функция, которая будет вызываться при команде /start
async def start(update: Update, context) -> None:
    # Кнопки меню
    keyboard = [
        ["Темперніт", "Поміч"],
        ["Кохання"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)

    # Приветственное сообщение с кнопками
    await update.message.reply_text(
        'Ну привіт',
        reply_markup=reply_markup
    )

# Функция, которая обрабатывает текстовые сообщения
async def handle_message(update: Update, context) -> None:
    text = update.message.text

    if text == "Темперніт":
        await update.message.reply_text("Книга ТЕМПЕРНІТ вийде у 2032 році...")
    elif text == "Поміч":
        await update.message.reply_text("Ну мені на шкокладку - 4441111132589031")
    elif text == "Кохання":
        await update.message.reply_text("Кохання не має.")
    else:
        await update.message.reply_text("КЛАЦАЙ ТІЛЬКІ ТЕ, ЩО Є!!")

# Основная функция для запуска бота
def main():
    application = Application.builder().token("7585432378:AAGhbYhZ24WrQ5SXUBkWy1r6GLS0rOpehG0").build()

    # Обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    try:
        application.run_polling()
    except NetworkError as e:
        print(f"Ошибка подключения: {e}. Попробуйте переподключиться.")

if __name__ == '__main__':
    main()