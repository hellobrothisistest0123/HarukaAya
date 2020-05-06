from math import ceil
from typing import List, Dict

from telegram import MAX_MESSAGE_LENGTH, InlineKeyboardButton, Bot, ParseMode
from telegram.error import TelegramError

from haruka import LOAD, NO_LOAD
from haruka.modules.translations.strings import tld
from telegram.ext import CommandHandler, Filters, MessageHandler, CallbackQueryHandler


class EqInlineKeyboardButton(InlineKeyboardButton):
    def __eq__(self, other):
        return self.text == other.text

    def __lt__(self, other):
        return self.text < other.text

    def __gt__(self, other):
        return self.text > other.text


def split_message(msg: str) -> List[str]:
    if len(msg) < MAX_MESSAGE_LENGTH:
        return [msg]

    else:
        lines = msg.splitlines(True)
        small_msg = ""
        result = []
        for line in lines:
            if len(small_msg) + len(line) < MAX_MESSAGE_LENGTH:
                small_msg += line
            else:
                result.append(small_msg)
                small_msg = line
        else:
            # Else statement at the end of the for loop, so append the leftover string.
            result.append(small_msg)

        return result


def paginate_modules(chat_id, page_n: int, module_dict: Dict, prefix, chat=None) -> List:
    if not chat:
        modules = sorted(
            [EqInlineKeyboardButton(tld(chat_id, x.__mod_name__),
                                    callback_data="{}_module({})".format(prefix, x.__mod_name__.lower())) for x
             in module_dict.values()])
    else:
        modules = sorted(
            [EqInlineKeyboardButton(tld(chat_id, x.__mod_name__),
                                    callback_data="{}_module({},{})".format(prefix, chat, x.__mod_name__.lower())) for x
             in module_dict.values()])

    pairs = list(zip(modules[::4], modules[4::3], modules[3::4]))

    if len(modules) % 4 == 3:
        pairs.append((modules[-1],))
    for i in range(0, len(modules) , 3):

    try : 
 
non = ( modules [ i ] , modules [ i + 1 ] . modules [ i + 2 ] ) 
 emp . append ( non ) 
except IndexError : 

 11 len ( modules ) % 3 = = 2 : 
 non = ( modules [ 1 ] . modules [ i + 1 ] . " ' ) 
 emp . append ( non ) 
 else : 
non modules [ i ] , " , " ' ) 
emp . append ( non ) 
 
 pairs = emp 
 max _ num _ pages = ceil ( len ( pairs ) / 8 ) 
 modulo _ page - page _ n % max _ num _ pages 

FR 
0 comments on commit ecdc2e0 
Write Preview 
AA Bi ( > EES @ RA 
Leave a comment 
Attach files by dragging & dropping , selecting or pasting them . 

