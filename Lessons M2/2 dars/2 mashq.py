from dataclasses import replace


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        info = f"Product name:{self.name}, price:{self.price}"

    @staticmethod
    def price_format(price):
        return format(1500, ","), replace(",", " ")


product = Product("Apple", 2000)
print(product)
