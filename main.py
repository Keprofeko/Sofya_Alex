
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# API токен бота
BOT_TOKEN = "8190423140:AAGB3m8bg-1SbGeD1Nrkb79bN2B-rfZAxFU"

# Ссылка на Google документ
GOOGLE_DOCS_LINK = "https://docs.google.com/document/d/1Ah4Syd4YazURl9aGO404rdhIlOxBjqa9NbV3UxNWTfs/edit?usp=sharing"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправляет приветствие и ссылку на Google документ по команде /start."""
    greeting = """Привет, ты на месте! 💥
Это тот самый гайд, который я бы вручила себе самой — если бы могла вернуться назад.
Тут не будет «ешь меньше — двигайся больше».
Тут будет:
— что ты делаешь не так, хотя стараешься
— почему ты не слабая, а просто устала
— как выстроить систему, которая держит — даже когда ты на нуле
📩 Лови гайд — и не теряйся."""
    
    await update.message.reply_text(greeting)
    await update.message.reply_text(f"Вот ссылка на документ:\n{GOOGLE_DOCS_LINK}")

async def send_link(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправляет ссылку на Google документ в ответ на любое сообщение."""
    await update.message.reply_text(
        f"Вот ссылка на документ:\n{GOOGLE_DOCS_LINK}"
    )

def main() -> None:
    """Запускает бота."""
    # Создаем приложение
    application = Application.builder().token(BOT_TOKEN).build()

    # Добавляем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, send_link))

    # Запускаем бота
    print("Бот запущен...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
