class Product:
    COUNT = 0
    CURRENT_DATE = "25.12.2022"

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.COUNT += 1
        self.product_id = self.__class__.COUNT

    def get_info(self):
        return f"Product name: {self.name}, price: {self.price}"


class Fruit(Product):
    def __init__(self, name, price, **kwargs):
        super().__init__(name, price)
        self.extra_data = kwargs

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}\nFruit data: {self.extra_data}"

    def is_expired(self):
        expire_date = self.extra_data.get("expire_date")
        return int(expire_date.split(".")[0]) < int(Product.CURRENT_DATE.split(".")[0])


class Vegetable(Product):
    def __init__(self, name, price, **kwargs):
        super().__init__(name, price)
        self.extra_data = kwargs

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}\nVegetable data: {self.extra_data}"

    def is_expired(self):
        expire_date = self.extra_data.get("expire_date")
        return int(expire_date.split(".")[0]) < int(Product.CURRENT_DATE.split(".")[0])


class Drink(Product):
    def __init__(self, name, price, **kwargs):
        super().__init__(name, price)
        self.extra_data = kwargs

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}\nDrink data: {self.extra_data}"

    def is_expired(self):
        expire_date = self.extra_data.get("expire_date")
        return int(expire_date.split(".")[0]) < int(Product.CURRENT_DATE.split(".")[0])


PRODUCT_TYPES = {
    1: Fruit,
    2: Vegetable,
    3: Drink,
}

products = []

while Product.COUNT < 3:
    product_type = int(input(
        f"Select product type:\n"
        f"1: {PRODUCT_TYPES.get(1).__name__}\n"
        f"2: {PRODUCT_TYPES.get(2).__name__}\n"
        f"3: {PRODUCT_TYPES.get(3).__name__}\n> "
    ))
    if product_type not in PRODUCT_TYPES.keys():
        print("Invalid product type!")
        continue
    ChildProduct = PRODUCT_TYPES.get(product_type)
    name = input("Enter product name: ")
    price = input("Enter product price: ")
    extra_data = {}
    YES_NO = ["Y", "N"]
    extra_data_answer = input(f"Enter extra data:\nYes({YES_NO[0]})\nCancel({YES_NO[1]})\n> ")
    if extra_data_answer != YES_NO[1]:
        expire_date = input("Enter expire date Ex: 25.11.2022\n> ")
        extra_data.update({"expire_date": expire_date})
    obj = ChildProduct(name, price, **extra_data)
    products.append(obj)
    print("products count", Product.COUNT)

expired_product_names = []

for product in products:
    print(product.product_id)
    if product.extra_data and product.is_expired():
        expired_product_names.append(product.name)

print(expired_product_names)