import logging
import traceback

from telegram import Update, CallbackQuery, InlineKeyboardMarkup
from telegram.ext import CallbackContext

import commands.inline_commands as incmd  # place for your inline commands
import commands.keyboards as kb
import utils.utils as utl

logger = logging.getLogger('my-bot')


def handle_callback(update: Update, context: CallbackContext):
    """
    :param update:
    :param context:
    Main handler for callback queries:\n
    - maps queries to matching command

    - handles 'query prefixes' like 'clear_' to clear inline keyboards
    - sends new message at the end, if needed
    :return:
    """
    # dict to map callback to function (str: function reference)
    command_switch = {
        # TODO: REGISTER INLINE COMMANDS HERE
        'foo': incmd.foo_command,
        'bar': incmd.bar_command,
    }

    # extract callback object
    query: CallbackQuery = update.callback_query
    query.answer()
    key = query.data

    # handle special prefixes
    if key.startswith('clear_'):
        query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup([[]]))
        key = key.replace('clear_', '')

    send_new_message = False  # to toggle a new message at the end
    if key.startswith('new_'):
        key = key.replace('new_', '')
        send_new_message = True

    # TODO: handle commands with special signature here
    # if key.startswith('complex_command'):
    #     command_switch['complex_command'](query, and, extra, content)

    try:
        # try to extract command
        command = command_switch[key]
        # check if command belongs to inline commands
        if command.__module__ == 'commands.inline_commands':
            command(query)

        # if standard commands shall be called from callback query
        # else:
        #     command(update, context)

        # send new menu if toggled
        if send_new_message:
            utl.send_msg(query, context, "What's next?", keyboard=kb.main_menu)

    # if we fail to extract the key
    except KeyError:
        logger.error(f"CAN'T FIND COMMAND {key} IN COMMAND_SWITCH\n{traceback.format_exc()}")
        print(f'{key} was NOT listed!')