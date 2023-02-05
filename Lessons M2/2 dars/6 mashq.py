class Car():

    def __init__(self, name, color, price, year, result):
        self.name = name
        self.color = color
        self.price = price
        self.year = year
        self.result = result
        self.result = f"Nome: {self.name}\nRangi: {self.color}\nNarxi: {self.price}\nYili: {self.year}"


result = ""
name = "Dodge"
color = "Red"
price = "250.000$"
year = "2017"
object = Car(name, color, price, year, result)
print(object.result)
