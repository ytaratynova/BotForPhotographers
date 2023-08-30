from .Inline import ikb_start
from .Inline import create_ikb_settings, create_ikb_albums, create_ikb_prices, ikb_confirm, create_ikb_prices, \
    create_ikb_package_details, create_ikb_admin, create_portfolio_navigation, create_ikb_change_album, create_ikb_change_packages,\
    create_ikb_for_mailing_list
from .Standart import create_kb_album, create_kb_package


__all__ = ['ikb_start',
           'create_ikb_settings',
           'create_ikb_albums',
           'create_ikb_prices',
           'ikb_confirm',
           'create_ikb_prices',
           'create_ikb_package_details',
           'create_ikb_admin', 'create_kb_album',
           'create_portfolio_navigation',
           'create_ikb_change_album',
           'create_ikb_change_packages',
           'create_ikb_for_mailing_list']