""""""
"""
1. Talaba klassini yarating va talaba ma'lumotlaridan konstruktor orqali obyekt yarating,
obyekt ma'lumotlarini chop eting.
"""


class Talaba:
    def __init__(self, name, surname, years, job):
        self.ism = name
        self.familiya = surname
        self.yosh = years
        self.yonalish = job


print('project-1')
ism = "MuhammadZohir"
familiya = "Roziyev"
yosh = 15
yonalish = "IT"

telaba_project1 = Talaba(ism, familiya, yosh, yonalish)

print(f"Name:{ism},"
      f"Surname:{familiya} "
      f"years:{yosh},"
      f" Job:{yonalish}")
