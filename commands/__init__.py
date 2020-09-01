from subtitle import (
    BASE_URL,
    get_lang,
    search_sub
)

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hi *{update.effective_user.first_name}*!\n\nI am subtitle downloader bot. I can provide movie subtitles.\n\n==> Just send me Movie name. Use @imdb or @imdbot inline to get currect movie name.\n\nSubscribe ℹ️ @Keralabotsnews if you ❤️ using this bot!", parse_mode="Markdown")

def searching(update: Update, context: CallbackContext):
    if update.message.via_bot != None:
        return

    search_message = context.bot.send_message(chat_id=update.effective_chat.id, text="Searching your subtitle file")
    sub_name = update.effective_message.text
    index, title, keyword = search_sub(sub_name)
    inline_keyboard = []
    if len(index) == 0:
        context.bot.edit_message_text(chat_id=update.effective_chat.id, message_id=search_message.message_id, text="No results found")
        return

    for i in index:
        subtitle = title[i-1]
        key = keyword[i-1]
        inline_keyboard.append([InlineKeyboardButton(subtitle, callback_data=f"{key}")])

    reply_markup = InlineKeyboardMarkup(inline_keyboard)
    context.bot.edit_message_text(chat_id=update.effective_chat.id, message_id=search_message.message_id, text=f"Got the following results for your query *{sub_name}*. Select the preffered type from the below options", parse_mode="Markdown", reply_markup=reply_markup)
