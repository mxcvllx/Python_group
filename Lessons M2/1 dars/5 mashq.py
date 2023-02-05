""""""
"""
5. 2 ta talaba ma'lumotlarini saqlaydigan klass yarating, bunda 1-class asosiy ma'lumotlar ismi,familyasi, tel raqami,
 2-class da o'qiydigan fanlar ro'yxati va baholari, o'rtacha bahosi, o'qishga kirgan yili, tugatadigan tili saqlansin. 
 Yaratilgan klass lar orqali obyektlar yarating va chop eting.
"""


class Talaba2:

    def __init__(self, fan1, fan2, fan3, baholar, oqish, til):
        self.fan1 = fan1
        self.fan2 = fan2
        self.fan3 = fan3
        self.baholar = baholar
        self.oqish = oqish
        self.til = til


class Talaba1:

    def __init__(self, name, surname, number):
        self.name = name
        self.surname = surname
        self.number = number


print('1 project')
name = "Abdusattor"
surname = "Halilov"
number = 998639009
talaba_ob1 = Talaba1(name, surname, number)
print(f"name: {name},"
      f"Surname: {surname},"
      f"number: {number}")


print('2 project')
fan1 = "Fizika"
fan2 = "matematika"
fan3 = "Tarih"
baholar = 4,5
oqish = "2020"
til = "Rus tili"
talaba_ob2 = Talaba2(fan1, fan2, fan3, baholar, oqish, til)
print(f"1 fan:{fan1},"
      f" "
      f"2 fan:{fan2},"
      f" "
      f"3 fan:{fan3},"
      f" "
      f"baholar:{baholar},"
      f" "
      f"oqish:{oqish},"
      f" "
      f"til:{til},"
      f" "
      )