import logging

from telegram import Update
from telegram.ext import CallbackContext

import utils.utils as utl
import commands.keyboards as kb
import database.db as db
from database.db import open_session

logger = logging.getLogger('my-bot')


def start(update: Update, context: CallbackContext):
    """
    Function to be called when user enters /start \n
    - Adds user to database if not already exists
    - sends greeting, chat id and help-text
    :param update: Telegram Update
    :param context: Telegram Context
    :return:
    """
    session = open_session()
    # prevent double entries
    # if return has entries - user is in database
    if utl.get_entries_by_chat_id(update.message.chat_id, database=db.Users):
        utl.send_msg(
            update, context,
            text=utl.prep_for_md(f"Hey, you're already registered.\nYou ID is: {update.message.chat_id}\n\n") +
            utl.get_help_text(),
            keyboard=kb.main_menu, parse_mode='MarkdownV2')
        return

    # add new user to database
    user = db.Users(chat_id=update.message.chat.id, username=update.message.chat.username,
                    menu='main', listen_mode='default')
    session.add(user)
    session.commit()
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text=utl.prep_for_md(f"Hi, you're now registered!\n" f"Your ID is: {update.message.chat.id}\n\n") +
        utl.get_help_text(),
        reply_markup=kb.main_menu, parse_mode='MarkdownV2')


def send_help(update: Update, context: CallbackContext):
    utl.send_msg(update, context, utl.get_help_text(), keyboard=kb.main_menu, parse_mode='MarkdownV2')

# TODO: REGISTER YOUR "SLASH" COMMANDS HERE
