class Class1:
    def __init__(self, name, id, point):
        self.name = name
        self.id = id
        self.point = point


class Class2:
    def __init__(self, annual_income, salary):
        self.annual_income = annual_income
        self.salary = salary


class Class3(Class1, Class2):
    def __init__(self, name, id, point, annual_income, salary, price):
        super().__init__(name, id, point)
        self.annual_income = annual_income
        self.salary = salary

    def main_info(self):
        return f"name:{self.name},  ID:{self.id},  point:{self.point},  annual_income:{self.annual_income},  salary:{self.salary}"

    def return_info(self):
        main_info = self.main_info()
        return f"Class info : {main_info}"


ob = Class3("phone", 564754, 560, "7.200$", "600$")
print(ob.return_info())
