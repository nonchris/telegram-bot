from telegram import CallbackQuery
from telegram.error import BadRequest

import utils.utils as utl
import commands.keyboards as kb


def foo_command(query: CallbackQuery):
    try:
        query.edit_message_text(
            utl.prep_for_md("This is *foo*", ignore=['*']),
            reply_markup=kb.main_menu,
            parse_mode='MarkdownV2')

    # text must be updated - if foo is hit twice and the text doesn't change, we'll receive a bad request
    except BadRequest as e:
        print("Bad request")
        print(e)


def bar_command(query: CallbackQuery):
    try:
        query.edit_message_text("This is bar", reply_markup=kb.main_menu)

    # text must be updated - if foo is hit twice and the text doesn't change, we'll receive a bad request
    except BadRequest as e:
        print("Bad request")
        print(e)

# TODO: ADD YOUR INLINE COMMANDS HERE
