from .Inline import ikb_start
from .Inline import create_ikb_settings, create_ikb_albums, create_ikb_prices, ikb_confirm, create_ikb_prices, \
    create_ikb_package_details, create_ikb_admin, create_portfolio_navigation, create_ikb_change_album, create_ikb_change_packages,\
    create_ikb_for_mailing_list, create_ikb_for_photographers_for_admin, create_ikb_for_photographers, create_ikb_video,\
    create_ikb_presets, create_ikb_product_details, create_ikb_with_newsletter

from .Standart import create_kb_album, create_kb_package, create_kb_product, create_kb_product_names


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
           'create_ikb_for_mailing_list',
           'create_ikb_for_photographers_for_admin',
           'create_ikb_for_photographers',
           'create_ikb_video', 'create_ikb_presets', 'create_kb_product', 'create_kb_product_names',
           'create_ikb_product_details', 'create_ikb_with_newsletter']