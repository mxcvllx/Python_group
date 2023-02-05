class Products:
    COUNT = 0


class Fruits(Products):
    def __init__(self, product_1, product_2, product_3, product_4, lst_1):
        super().__init__()
        self.product_1 = product_1
        self.product_2 = product_2
        self.product_3 = product_3
        self.product_4 = product_4
        self.lst_1 = lst_1

    def max_min_price(self):
        expensive_name = ""
        expensive_price = self.product_1['price']
        poor_name = ""
        poor_price = self.product_1['price']
        for i in self.lst_1:
            if i['price'] > expensive_price:
                expensive_price = i['price']
                expensive_name = i['name']
            else:
                poor_price = i['price']
                poor_name = i['name']
        return f"qimmat meva nomi: {expensive_name}, narxi: {expensive_price}\n arzon meva nomi: {poor_name}, narxi: {poor_price}"

    def color(self):
        dict_red = {}
        dict_yellow = {}
        dict_blue = {}
        dict_orange = {}
        dict_green = {}
        for i in self.lst_1:
            if i['color'] == "red":
                dict_red['id'] = i['id']
                dict_red['name'] = i['name']
            if i['color'] == "yellow":
                dict_yellow['id'] = i['id']
                dict_yellow['name'] = i['name']
            if i['color'] == "blue":
                dict_blue['id'] = i['id']
                dict_blue['name'] = i['name']
            if i['color'] == "orange":
                dict_orange['id'] = i['id']
                dict_orange['name'] = i['name']
            if i['color'] == "green":
                dict_green['id'] = i['id']
                dict_green['name'] = i['name']
        return f"Red: {dict_red},\nYellow: {dict_yellow},\nBlue: {dict_blue},\nOrange: {dict_orange},\nGreen: {dict_green}\n"


class Drinks(Products):
    def __init__(self, product_1, product_2, product_3, product_4, lst_2):
        super().__init__()
        self.product_1 = product_1
        self.product_2 = product_2
        self.product_3 = product_3
        self.product_4 = product_4
        self.lst_2 = lst_2

    def max_min_price(self):
        expensive_name = ""
        expensive_price = self.product_1['price']
        poor_name = ""
        poor_price = self.product_1['price']
        for i in self.lst_2:
            if i['price'] > expensive_price:
                expensive_price = i['price']
                expensive_name = i['name']
            else:
                poor_price = i['price']
                poor_name = i['name']
        return f"Qimmat ichimliklar nomi: {expensive_name}, narx: {expensive_price}\n arzon ichimlik nomi: {poor_name}, narx: {poor_price}"

    def color(self):
        dict_red = {}
        dict_yellow = {}
        dict_blue = {}
        dict_orange = {}
        dict_green = {}
        for i in self.lst_2:
            if i['color'] == "red":
                dict_red['id'] = i['id']
                dict_red['name'] = i['name']
            if i['color'] == "yellow":
                dict_yellow['id'] = i['id']
                dict_yellow['name'] = i['name']
            if i['color'] == "blue":
                dict_blue['id'] = i['id']
                dict_blue['name'] = i['name']
            if i['color'] == "orange":
                dict_orange['id'] = i['id']
                dict_orange['name'] = i['name']
            if i['color'] == "green":
                dict_green['id'] = i['id']
                dict_green['name'] = i['name']
        return f"Red: {dict_red},\nYellow: {dict_yellow},\nBlue: {dict_blue},\nOrange: {dict_orange},\nGreen: {dict_green}\n"


class Vegetables(Products):

    def __init__(self, product_1, product_2, product_3, product_4, lst_3):
        super().__init__()
        self.product_1 = product_1
        self.product_2 = product_2
        self.product_3 = product_3
        self.product_4 = product_4
        self.lst_3 = lst_3

    def max_min_price(self):
        expensive_name = ""
        expensive_price = self.product_1['price']
        poor_name = ""
        poor_price = self.product_1['price']
        for i in self.lst_3:
            if i['price'] > expensive_price:
                expensive_price = i['price']
                expensive_name = i['name']
            else:
                poor_price = i['price']
                poor_name = i['name']
        return f"Eng qimmat sabzavot nomi: {expensive_name}, narxi: {expensive_price}\n Eng arzon sabzavot nomi: {poor_name}, narxi: {poor_price}"

    def color(self):
        dict_red = {}
        dict_yellow = {}
        dict_blue = {}
        dict_orange = {}
        dict_green = {}
        for i in self.lst_3:
            if i['color'] == "red":
                dict_red['id'] = i['id']
                dict_red['name'] = i['name']
            if i['color'] == "yellow":
                dict_yellow['id'] = i['id']
                dict_yellow['name'] = i['name']
            if i['color'] == "blue":
                dict_blue['id'] = i['id']
                dict_blue['name'] = i['name']
            if i['color'] == "orange":
                dict_orange['id'] = i['id']
                dict_orange['name'] = i['name']
            if i['color'] == "green":
                dict_green['id'] = i['id']
                dict_green['name'] = i['name']
        return f"Red: {dict_red},\nYellow: {dict_yellow},\nBlue: {dict_blue},\nOrange: {dict_orange},\nGreen: {dict_green}\n"


fruit_product_1 = {
    "name": input("1 meva nomini kiriting: "),
    "id": "01",
    "color": input("1-meva rangini kiriting: "),
    "price": int(input("1-meva narxini kiriting: ")),
    "made_time": input("1-meva yaratilgan vaqtini kiriting: ")
}
fruit_product_2 = {
    "name": input("\n2-meva nomini kiriting: "),
    "id": "02",
    "color": input("2-meva rangini kiriting: "),
    "price": int(input("2-meva narxini kiriting: ")),
    "made_time": input("2-meva yaratilgan vaqtini kiriting: ")
}
fruit_product_3 = {
    "name": input("\n3-meva nomini kiriting: "),
    "id": "03",
    "color": input("3-meva rangini kiriting: "),
    "price": int(input("3-meva narxini kiriting: ")),
    "made_time": input("3-meva yaratilgan vaqtini kiriting: ")
}
fruit_product_4 = {
    "name": input("\n4-meva nomini kiriting: "),
    "id": "04",
    "color": input("4-meva rangini kiriting: "),
    "price": int(input("4-meva narxini kiriting: ")),
    "made_time": input("4-meva yaratilgan vaqtini kiriting: ")
}
lst_1 = [fruit_product_1, fruit_product_2, fruit_product_3, fruit_product_4]

drink_product_1 = {
    "name": input("1-ichimlik nomini kiriting: "),
    "id": "05",
    "color": input("1-ichimlik rangini kiriting: "),
    "price": int(input("1-ichimlik narxini kiriting: ")),
    "made_time": input("1-ichimlik yaratilgan vaqtini kiriting: ")
}
drink_product_2 = {
    "name": input("\n2-ichimlik nomini kiriting: "),
    "id": "06",
    "color": input("2-ichimlik rangini kiriting: "),
    "price": int(input("2-ichimlik narxini kiriting: ")),
    "made_time": input("2-ichimlik yaratilgan vaqtini kiriting: ")
}
drink_product_3 = {
    "name": input("\n3-ichimlik nomini kiriting: "),
    "id": "07",
    "color": input("3-ichimlik rangini kiriting: "),
    "price": int(input("3-ichimlik narxini kiriting: ")),
    "made_time": input("3-ichimlik yaratilgan vaqtini kiriting: ")
}
drink_product_4 = {
    "name": input("\n4-ichimlik nomini kiriting: "),
    "id": "08",
    "color": input("4-ichimlik rangini kiriting: "),
    "price": int(input("4-ichimlik narxini kiriting: ")),
    "made_time": input("4-ichimlik yaratilgan vaqtini kiriting: ")
}
lst_2 = [drink_product_1, drink_product_2, drink_product_3, drink_product_4]

vegetable_product_1 = {
    "name": input("1-sabzavot nomini kiriting: "),
    "id": "09",
    "color": input("1-sabzavot rangini kiriting: "),
    "price": int(input("1-sabzavot narxini kiriting: ")),
    "made_time": input("1-sabzavot yaratilgan vaqtini kiriting: ")
}
vegetable_product_2 = {
    "name": input("\n2-sabzavot nomini kiriting: "),
    "id": "10",
    "color": input("2-sabzavot rangini kiriting: "),
    "price": int(input("2-sabzavot narxini kiriting: ")),
    "made_time": input("2-sabzavot yaratilgan vaqtini kiriting: ")
}
vegetable_product_3 = {
    "name": input("\n3-sabzavot nomini kiriting: "),
    "id": "11",
    "color": input("3-sabzavot rangini kiriting: "),
    "price": int(input("3-sabzavot narxini kiriting: ")),
    "made_time": input("3-sabzavot yaratilgan vaqtini kiriting: ")
}
vegetable_product_4 = {
    "name": input("\n4-sabzavot nomini kiriting: "),
    "id": "12",
    "color": input("4-sabzavot rangini kiriting: "),
    "price": int(input("4-sabzavot narxini kiriting: ")),
    "made_time": input("4-sabzavot yaratilgan vaqtini kiriting: ")
}
lst_3 = [vegetable_product_1, vegetable_product_2, vegetable_product_3, vegetable_product_4]

fruits = Fruits(fruit_product_1, fruit_product_2, fruit_product_3, fruit_product_4, lst_1)
drinks = Drinks(drink_product_1, drink_product_2, drink_product_3, drink_product_4, lst_2)
vegetables = Vegetables(vegetable_product_1, vegetable_product_2, vegetable_product_3, vegetable_product_4, lst_3)

print(fruits.max_min_price())
print(fruits.color())

print(drinks.max_min_price())
print(drinks.color())

print(vegetables.max_min_price())
print(vegetables.color())
