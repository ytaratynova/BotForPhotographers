from aiogram.dispatcher.filters.state import StatesGroup, State


class NewPackage(StatesGroup):
    name = State()
    poster1 = State()
    poster2 = State()
    confirm = State()

class NewAlbum(StatesGroup):
    name = State()
    confirm = State()

class NewPhoto(StatesGroup):
    album = State()
    photo = State()
    confirm = State()

class DellAlbum(StatesGroup):
    name = State()
    confirm = State()

class DellPhoto(StatesGroup):
    name = State()
    id = State()
    confirm = State()

class DellPackage(StatesGroup):
    name = State()
    confirm = State()

class SendSaleInfo(StatesGroup):
    name = State()
    confirm = State()
