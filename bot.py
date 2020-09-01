import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

logger = logging.getLogger(__name__)

from config import BOT_TOKEN

from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    Filters,
    InlineQueryHandler
)

from commands import (
    start,
    searching
)

from inline import(
    button,
    inlinequery
)


def main():
    updater = Updater(token=BOT_TOKEN, use_context=True, workers=8)
    logger.info(f"SUCESSFULLY STARTED THE BOT IN {updater.bot.username}")
    start_handler = CommandHandler('start', start)
    search_handler = MessageHandler(Filters.text, searching)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(search_handler)
    dispatcher.add_handler(CallbackQueryHandler(button))
    dispatcher.add_handler(InlineQueryHandler(inlinequery))
    updater.start_polling()
    updater.idle()
    updater.stop()


if __name__ == "__main__":
    main()
