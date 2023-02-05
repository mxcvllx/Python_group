""""""
"""
4. Mashina klass yarating va classdan 10 ta obyekt yarating. Yaratilgan obyektlar orasida ishlab
 chiqarilganiga 10 yildan oshgan markalar bo'lsa chop eting.
"""


class Car:

    def __init__(self, brand, color, year):
        print(brand, color, year)
        self.brand = brand
        self.color = color
        self.year = year


print("1-project")
brand = "Toyota"
color = "White"
year = 2010

car_object1 = Car(brand, color, year)
print(f"Marka:{brand}, "
      f"color:{color},"
      f"year:{year}")


print("2-project")
brand = "Hyundai"
color = "red"
year = 2015

car_object2 = Car(brand, color, year)
print(f"Marka:{brand}, "
      f"color:{color},"
      f"year:{year}")



print("3-project")
brand = "BMW"
color = "Blue"
year = 2022

car_object3 = Car(brand, color, year)
print(f"Marka:{brand},"
      f"color:{color},"
      f"year:{year}")


print("4-project")
brand = "Mercedez"
color = "Black"
year = 1999

car_object4 = Car(brand, color, year)
print(f"Marka:{brand},"
      f"color:{color},"
      f"year:{year}")


print("5-project")
brand = "Tesla"
color = "White"
year = 2022

car_object5 = Car(brand, color, year)
print(f"Marka:{brand},"
      f"color:{color},"
      f"year:{year}")

