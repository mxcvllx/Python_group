class Komputer:
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

    def return_info(self):
        main_info = self.main_info()
        return f"Pc info - {main_info}"


computer1 = Komputer("HP", 1200, "blue", "HP", "1tb", "2023", "USA")
computer2 = Komputer("ROG", 600, "blue", "ASUS", "1tb", "2023", "USA")
computer3 = Komputer("MIC", 760, "blue", "Microsof", "1tb", "2023", "USA")
computer4 = Komputer("Imac", 1550, "blue", "Apple", "1tb", "2023", "USA")
computer5 = Komputer("Pavilion", 1230, "blue", "HP", "1tb", "2023", "USA")
computer6 = Komputer("game", 860, "blue", "ASUS", "1tb", "2023", "USA")
computer7 = Komputer("Deck", 600, "blue", "Steam", "1tb", "2023", "USA")
computer8 = Komputer("turbo", 1690, "blue", "ASUS", "1tb", "2023", "USA")
computer9 = Komputer("LC", 2300, "blue", "HP", "1tb", "2023", "USA")
computer10 = Komputer("mac", 900, "blue", "Apple", "1tb", "2023", "USA")

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
