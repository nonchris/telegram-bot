import os
import logging

from telegram import Bot
from telegram import error
from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram.ext import MessageHandler, Filters

import commands.commands as cmd
import commands.handle_callback as clb
import commands.on_message as on_msg

# set logging format
formatter = logging.Formatter("[{asctime}] [{levelname}] [{name}] {message}", style="{")

# logger for writing to file
file_logger = logging.FileHandler('data/events.log')
file_logger.setLevel(logging.INFO)  # everything into the logging file
file_logger.setFormatter(formatter)

# logger for console prints
console_logger = logging.StreamHandler()
console_logger.setLevel(logging.WARNING)  # only important stuff to the terminal
console_logger.setFormatter(formatter)

# get new logger
logger = logging.getLogger('my-bot')
logger.setLevel(logging.INFO)

# register loggers
logger.addHandler(file_logger)
logger.addHandler(console_logger)


# START BOT
# TODO: SET YOU API KEY AS ENV VARIABLE
API_Key = os.environ["API_KEY"]

updater = Updater(API_Key, use_context=True)
dispatcher = updater.dispatcher

bot = Bot(token=API_Key)

# add on message listener
dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), on_msg.handle_message))

# TODO: REGISTER NEW "SLASH" COMMANDS HERE, like /start or /help
dispatcher.add_handler(CommandHandler(['start'], cmd.start))

dispatcher.add_handler(CommandHandler(['help', 'h'], cmd.send_help))

# responsible for all inline commands
dispatcher.add_handler(CallbackQueryHandler(clb.handle_callback))

updater.start_polling()
updater.idle()
