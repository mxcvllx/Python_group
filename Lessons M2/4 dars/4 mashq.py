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


class Bus(Transports):
    def __init__(self, name, color, move_road, speed, type_bus):
        super().__init__(name, color, move_road)
        self.speed = speed
        self.type_bus = type_bus

    def main_info(self):
        return f"Name: {self.name},color: {self.color}, Movement type: {self.move_road}, speed:{self.speed}" \
               f"type_bus:{self.type_bus}"

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
    def __init__(self, name, color, move_road, speed, type_train):
        super().__init__(name, color, move_road)
        self.speed = speed
        self.type_train = type_train

    def main_info(self):
        return f"Name: {self.name}, color: {self.color}, Movement type: {self.move_road}, speed: {self.speed}," \
               f"type_train:{self.type_train}"

    def return_info(self):
        main_info = self.main_info()
        return f"Transport info- {main_info}"


car = Car("Malibu (CAr)", "Black", "Asphalt", '220km')
bus = Bus("Hyundai", "Green", "Asphalt", "120km", "electrobus")
underground = Underground("Akron (metro)", "black", "flight", "Speed")
tran = Train("Afrosiyob", "White", "fligth", "Spped", "electro")

print(car.return_info())
print(bus.return_info())
print(underground.return_info())
print(tran.return_info())
