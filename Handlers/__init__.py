from .start import ikb_start
from .start import dp
from .settings import dp, create_ikb_settings, select_settings
from .portfolio import dp, create_ikb_albums
from .prices import dp, create_ikb_prices
from .cancel_fsm import dp
from .new_package import dp
from .new_album import dp
from .dell_album import dp
from .new_photo import dp
from .del_photo import dp
from .del_package import dp
from .order import dp
from .admin import dp, create_ikb_admin
from .all import dp



__all__ = ['dp', 'ikb_start', 'create_ikb_settings', 'select_settings', 'create_ikb_albums', 'new_photo',
           'create_ikb_prices',
           'create_ikb_admin',
           'order',
           'del_photo',
           'del_package',
           'dell_album']