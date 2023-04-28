class Computer:
    def __init__(self, name, price, color, brand_name, ram, prodaction_year, region):
        self.name = name
        self.price = price
        self.color = color
        self.brand_name = brand_name
        self.ram = ram
        self.prodaction_year = prodaction_year
        self.region = region

    def main_info(self):
        return f"Name pc:{self.name}, " \
               f"price pc:{self.price}," \
               f"color pc:{self.color}," \
               f"brand name:{self.brand_name}," \
               f"ram pc:{self.ram}," \
               f"prodaction year:{self.prodaction_year}," \
               f"region:{self.region}"

    def pc_price(self):
        price = 1550
        price2 = 600
        for i in self.price:
            if i > price:
                return f"eng kimmat pc{self.price}"
            if i < price2:
                return f"eng arzon pc{self.price}"

    def return_info(self):
        pc_price = self.pc_price()
        main_info = self.main_info()
        return f"Pc info - {main_info}," \
               f"pc price - {pc_price}"


computer1 = Computer("HP", 1200, "blue", "HP", "1tb", "2023", "USA")
computer2 = Computer("ROG", 600, "blue", "ASUS", "1tb", "2023", "USA")
computer3 = Computer("MIC", 760, "blue", "Microsof", "1tb", "2023", "USA")
computer4 = Computer("Imac", 1550, "blue", "Apple", "1tb", "2023", "USA")
computer5 = Computer("Pavilion", 1230, "blue", "HP", "1tb", "2023", "USA")
computer6 = Computer("game", 860, "blue", "ASUS", "1tb", "2023", "USA")
computer7 = Computer("Deck", 600, "blue", "Steam", "1tb", "2023", "USA")
computer8 = Computer("turbo", 1690, "blue", "ASUS", "1tb", "2023", "USA")
computer9 = Computer("LC", 2300, "blue", "HP", "1tb", "2023", "USA")
computer10 = Computer("mac", 900, "blue", "Apple", "1tb", "2023", "USA")

print(computer1.return_info())
print(computer2.return_info())
print(computer3.return_info())
print(computer4.return_info())
print(computer5.return_info())
print(computer6.return_info())
print(computer7.return_info())
print(computer8.return_info())
print(computer9.return_info())
print(computer10.return_info())


