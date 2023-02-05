class Transports:
    def __init__(self, name, color, move_road):
        self.name = name
        self.color = color
        self.move_road = move_road


class Car(Transports):
    def __init__(self, name, color, move_road, speed):
        super().__init__(name, color, move_road)
        self.speed = speed

    def main_info(self):
        return f"Name: {self.name}, color: {self.color}, Movement type: {self.move_road}, speed: {self.speed}"

    def return_info(self):
        main_info = self.main_info()
        return f"Transport info - {main_info}"

    @property
    def change(self):
        return self.color

    @change.setter
    def change(self, value):
        self.color = value


class Car(Transports):
    def __init__(self, name, color, move_road, speed):
        super().__init__(name, color, move_road)
        self.speed = speed

    def main_info(self):
        return f"Name: {self.name}, color: {self.color}, Movement type: {self.move_road}, speed: {self.speed}"

    def return_info(self):
        main_info = self.main_info()
        return f"Transport info - {main_info}"


class Bus(Transports):
    def __init__(self, name, color, move_road, speed):
        super().__init__(name, color, move_road)
        self.speed = speed

    def main_info(self):
        return f"Name: {self.name},color: {self.color}, Movement type: {self.move_road}, speed:{self.speed}"

    def return_info(self):
        main_info = self.main_info()
        return f"Transport info - {main_info}"


class Underground(Transports):
    def __init__(self, name, color, move_road, speed):
        super().__init__(name, color, move_road)
        self.speed = speed

    def main_info(self):
        return f"Name: {self.name}, color: {self.color}, Movement type: {self.move_road}, speed: {self.speed}"

    def return_info(self):
        main_info = self.main_info()
        return f"Transport info - {main_info}"


class Train(Transports):
    def __init__(self, name, color, move_road, speed):
        super().__init__(name, color, move_road)
        self.speed = speed

    def main_info(self):
        return f"Name: {self.name}, color: {self.color}, Movement type: {self.move_road}, speed: {self.speed}"

    def return_info(self):
        main_info = self.main_info()
        return f"Transport info- {main_info}"


car = Car("Malibu (CAr)", "Black", "Asphalt", '220km')
bus = Bus("Hyundai (electrobus)", "Green", "Asphalt", "120km")
underground = Underground("Akron (metro)", "black", "flight", "Speed")
tran = Train("Afrosiyob (train)", "White", "fligth", "Spped")

print(car.return_info())
print(bus.return_info())
print(underground.return_info())
print(tran.return_info())