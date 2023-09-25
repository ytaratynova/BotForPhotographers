from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from Keyboards.Callback import main_menu, for_photographers
from loader import product_db



def create_ikb_for_photographers():

    ikb_for_photographers = InlineKeyboardMarkup(row_width=1)
    ibtn_video = InlineKeyboardButton(text="Видеоуроки",
                                  callback_data=for_photographers.new(menu='for_photographers', button='video'))
    ibtn_presets = InlineKeyboardButton(text="Пресеты",
                                      callback_data=for_photographers.new(menu='for_photographers', button='presets'))

    ibtn_back = InlineKeyboardButton(text='Назад',
                                     callback_data=main_menu.new(menu='main', button='back'))

    ikb_for_photographers.add(ibtn_video)
    ikb_for_photographers.add(ibtn_presets)
    ikb_for_photographers.add(ibtn_back)
    return ikb_for_photographers


def create_ikb_video(type):
    ikb_video = InlineKeyboardMarkup(row_width=1)
    video_list = [video[2] for video in product_db.select_product(type)]
    for video in video_list:
        ibtn=InlineKeyboardButton(text=video,
                                  callback_data=for_photographers.new(menu='video', button=video))
        ikb_video.add(ibtn)
    ibtn_back = InlineKeyboardButton(text='Назад',
                                     callback_data=main_menu.new(menu='main', button='back'))
    ikb_video.add(ibtn_back)
    return ikb_video


def create_ikb_presets(type):
    ikb_presets = InlineKeyboardMarkup(row_width=1)
    presets_list = [preset[2] for preset in product_db.select_product(type)]
    for preset in presets_list:
        ibtn=InlineKeyboardButton(text=preset,
                                  callback_data=for_photographers.new(menu='video', button=preset))
        ikb_presets.add(ibtn)
    ibtn_back = InlineKeyboardButton(text='Назад',
                                     callback_data=main_menu.new(menu='main', button='back'))
    ikb_presets.add(ibtn_back)
    return ikb_presets