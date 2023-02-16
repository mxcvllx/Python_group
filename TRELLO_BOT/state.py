from telebot.handler_backends import StatesGroup, State


class CreateNewTask(StatesGroup):
    boards = State()
    list = State()
    name = State()
    description = State()
    members = State()
    labels = State()
    date = State()