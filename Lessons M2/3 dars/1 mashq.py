class Product:
    def __init__(self, name, color, price, model):
        self.name = name
        self.color = color
        self.price = price
        self.model = model

    @property
    def change_model(self):
        return self.model

    @change_model.setter
    def change_model(self, value):
        self.model = value

    @property
    def price_(self):
        return self.price

    @price_.setter
    def price_(self, value):
        self.price = value

    @property
    def change_name(self):
        return self.name

    @change_name.setter
    def change_name(self, value):
        self.name = value

    @property
    def change_color(self):
        return self.color

    @change_model.setter
    def change_model(self, value):
        self.color = value

    def get_info(self):
        info = f"{self.name}, {self.color}, {self.price}, {self.model}"
        return info


product = Product("Phone", 'white', 640, 'M40')

print(product.price_)
name = "iphone"
color = "Black"
lst = 1244
model = "13 Ultra"
new_price = 890
product.price = new_price
product.model = model
product.color = color
product.name = name

print(Product.get_info(product))
