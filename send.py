import telegram
import os
import time

botToken = ""
bot = telegram.Bot(token=botToken)
chat_id = ""
bot.send_photo(chat_id=chat_id, caption= CAPTION, photo=open(file_path, 'rb'))


file_path = ""



from telegram.ext import Updater
updater = Updater(token=botToken, use_context=True)
dispatcher = updater.dispatcher
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)



updater.start_polling()

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)

from telegram import InlineQueryResultArticle, InputTextMessageContent
def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)

from telegram.ext import InlineQueryHandler
inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)



# TEXT = "Guten Tag,\n\nich bin Futterkatzebot. Mein Schöpfer ist Pascal Blansche.\nIch werde Sie in Zukunft über die Anwesenheit Ihrer Tageskatzen informieren.\nMit freundlichen Grüßen\nFutterkatzenbot"
# print(TEXT)

# bot.send_message(chat_id=chat_id, text=TEXT)
# bot.send_photo(chat_id=chat_id, photo=open(file_path, 'rb'))

# while True:
#     time.sleep(5)
#     if [u.message.text for u in updates][-1] == "test":
#         bot.send_message(chat_id=chat_id, text="Hello User")
#         chat_id = bot.get_updates()[-1].message.chat_id
#         bot.send_photo(chat_id=chat_id, photo=open(file_path, 'rb'))

# chat_id = bot.get_updates()[-1].message.chat_id
# bot.send_photo(chat_id=chat_id, photo=open(file_path, 'rb'))
