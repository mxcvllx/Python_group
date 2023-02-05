class Technologies:
    def __init__(self, name, made_year, garantiya_yaer):
        self.name = name
        self.made_year = made_year
        self.garantiya_year = garantiya_yaer


class Computer(Technologies):
    def __init__(self, name, made_year, garantiya_yaer, price, color, CPU):
        super().__init__(name, made_year, garantiya_yaer)
        self.price = price
        self.color = color
        self.CPU = CPU

    def main_info(self):
        return f"Name:{self.name}, year: {self.made_year}, Grant: {self.garantiya_year} price: {self.price} color: {self.color}, " \
               f"CPU:{self.CPU}"

    def return_info(self):
        main_info = self.main_info()
        return f"techno info - {main_info}"


class Phone(Technologies):
    def __init__(self, name, made_year, garantiya_yaer, price, color, CPU):
        super().__init__(name, made_year, garantiya_yaer)
        self.price = price
        self.color = color
        self.CPU = CPU

    def main_info(self):
        return f"Name: {self.name}, year: {self.made_year}, Grant: {self.garantiya_year}, price: {self.price} color: {self.color}" \
               f"CPU:{self.CPU}"

    def return_info(self):
        main_info = self.main_info()
        return f"techni info - {main_info}"


class Tv(Technologies):
    def __init__(self, name, made_year, garantiya_yaer, price, color, tv_type):
        super().__init__(name, made_year, garantiya_yaer)
        self.price = price
        self.color = color
        self.tv_type = tv_type

    def main_info(self):
        return f"Name: {self.name}, year: {self.made_year}, Garant: {self.garantiya_year}, price: {self.price}, color: {self.color}" \
               f"tv_type;{self.tv_type}"

    def return_info(self):
        main_info = self.main_info()
        return f"Techno info - {main_info}"


computer = Computer("Zalman", 2020, 5, "1.240$", "Green.and.Black", "core i9")
phone = Phone("Black Shark", 2022, 10, "600$", "Black", 'Snapdragon 8')
tv = Tv("Samsung", 2020, 6, "2.000$", "White", "smartTV")

print(computer.return_info())
print(phone.return_info())
print(tv.return_info())
