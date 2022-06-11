# import requests
from aiogram.types import   InlineKeyboardButton, InlineKeyboardMarkup

import data.config as cfg

btnUrlChanel = InlineKeyboardButton(text="Bizning kanal", url=cfg.CHANEL_URL)

channel_menu = InlineKeyboardMarkup(row_width=1).insert(btnUrlChanel)

# API_LINK = f'https://api.telegram.org/bot5259179545:AAF9qGo4CHeTlGpBhfDryEzXYlmrb-IBBOM'
# updates = requests.get(API_LINK + '/getUpdates?offset=-1').json()
# print(updates)