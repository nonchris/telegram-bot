from telegram import InlineKeyboardMarkup, InlineKeyboardButton

# TODO: CONFIGURE YOUR INLINE  BELOW

# prefixes (to be used in this order only)
# clear_ clear inline keyboard on current message
# new_ send a new main menu when command was executed
main_menu = InlineKeyboardMarkup([[InlineKeyboardButton('foo_cmd', callback_data='foo'),
                                   InlineKeyboardButton('bar_cmd', callback_data='bar'),
                                   # Sub menu not activated
                                   # InlineKeyboardButton('More', callback_data='more'),
                                   ]])

# From here: Completely functional sub-keyboard but not used
back_button = InlineKeyboardButton(u'\u2B05', callback_data='back')

more_menu = InlineKeyboardMarkup([[
    back_button,
    InlineKeyboardButton('sub_foo', callback_data='foo_2')
]])
