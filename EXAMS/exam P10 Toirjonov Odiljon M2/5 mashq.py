class Laptop:
    def __int__(self, monytor, ram, hdd, ssd):
        self.monytor = monytor
        self.ram = ram
        self.hdd = hdd
        self.ssd = ssd


class Komputer(Laptop):
    def __int__(self, monytor, ram, hdd, ssd, name, color, price):
        super().__int__(self.monytor, self.ram, self.hdd, self.ssd)
        self.monytor = monytor
        self.ram = ram
        self.hdd = hdd
        self.ssd = ssd
        self.name = name
        self.color = color
        self.price = price

    def get_name(self):
        return f"monitor:{self.monytor}, ram:{self.ram}, hdd:{self.hdd}, ssd:{self.ssd}" \
               f"name:{self.name}, color:{self.color}, price:{self.price}"

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
