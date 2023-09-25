from aiogram.utils.callback_data import CallbackData

main_menu = CallbackData('main_menu', 'menu', 'button')

settings = CallbackData('settings_option', 'menu', 'button')

portfolio_menu = CallbackData('portfolio', 'menu', 'button')

for_photographers = CallbackData('for_photographers', 'menu', 'button')

portfolio_menu_photos = CallbackData('photos', 'menu', 'button', 'album', 'cur_id')

price_menu = CallbackData('price_menu', 'menu', 'button')

price_menu_details = CallbackData('price_menu_details', 'menu', 'button', 'package')

confirm_request = CallbackData('confirm', 'menu', 'args', 'button')

admin_menu = CallbackData('admin_menu', 'menu', 'button')