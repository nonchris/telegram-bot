from typing import Union, List

from sqlalchemy import select
from sqlalchemy.engine import Row
from telegram import Update, CallbackQuery
from telegram.ext import CallbackContext

import database.db as db


def send_msg(update: Union[Update, CallbackQuery], context: CallbackContext, text, keyboard=None, parse_mode=''):
    if parse_mode == 'md':
        parse_mode = 'MarkdownV2'
    context.bot.send_message(chat_id=update.message.chat_id,
                             reply_markup=keyboard,
                             text=text,
                             parse_mode=parse_mode)


def prep_for_md(text: str, ignore=None) -> str:
    """
    :param text: string to be treated
    :param ignore: List with symbols (str) that shall not be replaced
    :return: string with escaped symbols

    - Escapes all symbols that have a special meaning in telegrams MarkdownV2\n
    - Selected symbols can be ignored by passing them into the function as list\n
    e.g. ['*', '_'] those symbols will not be escaped to be interpreted as italics / bold\n

    See: https://core.telegram.org/bots/api#markdownv2-style
    """

    symbols = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
    if ignore:
        for s in ignore:
            symbols.remove(s)

    for s in symbols:
        # print(f'{s}', '\{}'.format(s))
        text = text.replace(f'{s}', '\{}'.format(s))
    return text


def get_entries_by_chat_id(chat_id: int, database=db.Users) -> List[Union[db.Users]]:
    """
    :param chat_id: telegram chat id
    :param database: Reference to model class of database to be accessed\n
    e.g. database.Users
    :return: List of all matching entries as Objects of given database model
    """

    # get entries from entered database
    session = db.open_session()
    statement: List[Row] = select(database).where(database.chat_id == chat_id)

    # extract entry objects from row objects
    entries = [e[0] for e in session.execute(statement).all()]
    return entries


# TODO: UPDATE YOUR HELP MESSAGE HERE
# useful if help-text shall be sent from different places
def get_help_text() -> str:
    """:return: central help text in markdown style"""
    return prep_for_md("This is the place for *your custom help text*.\n\nThanks for using my template btw!\n_chris_",
                       ignore=['_', '*'])
