from telebot.handler_backends import State, StatesGroup


class StudentRegistrationForm(StatesGroup):
    first_name = State()
    last_name = State()
    phone = State()
    age = State()
    language = State()
    course = State()