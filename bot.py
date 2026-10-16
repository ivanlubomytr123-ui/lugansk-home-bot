
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        "Привет! 🏠 Я помогу найти квартиру "
        "посуточно в Луганске."
    )


def main():
    app = (
        Application.builder()
        .token("ВСТАВИТЬ_ТОКЕН")
        .build()
    )

    app.add_handler(CommandHandler("start", start))

    print("Бот запущен!")
    app.run_polling()


if __name__ == "__main__":
    main()
