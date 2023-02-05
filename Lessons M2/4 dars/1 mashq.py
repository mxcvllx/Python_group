class University:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


class Director(University):
    def __init__(self, name, surname, age, work_year):
        super().__init__(name, surname, age)
        self.work_year = work_year

    def main_info(self):
        return f"name: {self.name}, Surname: {self.surname}, age: {self.age}, certificate: {self.work_year}"

    def return_info(self):
        main_info = self.main_info()
        return f"Director info: {main_info}"


class Teacher(University):
    def __init__(self, name, surname, age, certificate):
        super().__init__(name, surname, age)
        self.certificate = certificate

    def main_info(self):
        return f"name: {self.name}, Surname: {self.surname}, age: {self.age}, certificate: {self.certificate}"

    def return_info(self):
        main_info = self.main_info()
        return f"Teacher info: {main_info}"


class Student(University):
    def __init__(self, name, surname, age, course):
        super().__init__(name, surname, age)
        self.course = course

    def main_info(self):
        return f"name: {self.name}, surname: {self.surname}, name: {self.age}, certificate: {self.course}"

    def return_info(self):
        main_info = self.main_info()
        return f"Student info: {main_info}"


director = Director("Anvar", "Obidjonov", 43, 16)
teacher = Teacher("Go'zal", "Jamshidova", 31, "Oliy ta'lim professori")
student = Student("Shoxjahon", "Akmalov", 23, "3-kurs")

print(director.return_info())
print(teacher.return_info())
print(student.return_info())