from telegram import Update
from telegram.ext import CallbackContext

import commands.keyboards as kb
import utils.utils as utl


def handle_message(update: Update, context: CallbackContext):
    """
    :param update: Telegram Update Object
    :param context: Telegram CallBackContext Object
    Handle messages sent to the bot.\n
    :return:
    """
    # TODO: YOUR MESSAGE HANDLING HERE
    utl.send_msg(update, context, "Hey!\nWhat can I do for you", kb.main_menu)
