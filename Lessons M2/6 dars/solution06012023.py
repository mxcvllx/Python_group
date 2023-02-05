class Person:
    COUNT = 0

    def __init__(self, name, age, region, phone_number, passport_seria_number):
        self.name = name
        self.age = age
        self.region = region
        self.__phone_number = phone_number
        self.__passport_seria_number = passport_seria_number
        Person.COUNT += 1
        self.person_id = Person.COUNT

    def __get_private_info(self):
        return f"Passport info: {self.__passport_seria_number}\nTel: {self.__phone_number}"

    def display(self):
        return f"Main info -> Name: {self.name}\nAge: {self.age}, Region: {self.region}, " \
               f"Private info: {self.__get_private_info()}"

    def update(self, **kwargs):
        # update(name="new name")
        for k, v in kwargs.items():
            if k == "__phone_number":
                self.__phone_number = v
            elif k == "__passport_seria_number":
                self.__passport_seria_number = v
            else:
                setattr(self, k, v)


class Teacher(Person):
    def __init__(self, name, age, region, phone_number, passport_seria_number, **teacher_data):
        super().__init__(name, age, region, phone_number, passport_seria_number)
        self.teacher_data = teacher_data

    def display(self):
        main_info = super().display()
        return f"Main info: {main_info}\nTeacher data: {self.teacher_data}"

    @classmethod
    def create(cls, name, age, region, phone_number, passport_seria_number, **teacher_data):
        return cls(name, age, region, phone_number, passport_seria_number, **teacher_data)


class Student(Person):
    def __init__(self, name, age, region, phone_number, passport_seria_number, **student_data):
        super().__init__(name, age, region, phone_number, passport_seria_number)
        self.subjects_data = student_data

    def display(self):
        main_info = super().display()
        return f"Main info: {main_info}\nTeacher data: {self.subjects_data}"

    def __subjects_count(self):
        return len(self.subjects_data)

    def __marks_sum(self):
        return sum(self.subjects_data.values())

    def marks_average(self):
        return round(self.__marks_sum() / self.__subjects_count(), 2)

    @classmethod
    def create(cls, name, age, region, phone_number, passport_seria_number, **subjects_data):
        return cls(name, age, region, phone_number, passport_seria_number, **subjects_data)


class Staff(Person):
    def __init__(self, name, age, region, phone_number, passport_seria_number, **staff_data):
        super().__init__(name, age, region, phone_number, passport_seria_number)
        self.staff_data = staff_data

    def display(self):
        main_info = super().display()
        return f"Main info: {main_info}\nTeacher data: {self.staff_data}"

    @classmethod
    def create(cls, name, age, region, phone_number, passport_seria_number, **staff_data):
        return cls(name, age, region, phone_number, passport_seria_number, **staff_data)


teachers = []
students = []
staff = []

PERSON_CLASSES = {
    1: Teacher,
    2: Student,
    3: Staff
}

REGIONS = {
    1: "Tashkent",
    2: "Fergana",
    3: "Andijan",
    4: "Namangan",
    5: "Syrdarya",
    6: "Jizzakh",
    7: "Samarkand",
    8: "Kashkadarya",
    9: "UZB"
}


def get_region():
    while True:
        region_id = int(input("Enter name: "))
        if region_id not in REGIONS:
            print("Invalid region id")
        else:
            region = REGIONS.get(region_id)
            break
    return region


def get_extra_data():
    data = {}
    VALID_ANSWER = {"y": "YES", "n": "NO"}
    while True:
        key = input("Enter key: ")
        value = input("Enter value: ")
        data.update({key: value})
        answer = input("Do you want to add new data? Y/N").lower()
        if answer not in VALID_ANSWER:
            print("Invalid answer")
        else:
            if answer == "y":
                continue
            elif answer == "n":
                break
    return data

# while Person.COUNT < 3:
#     selected_class_number = int(input(
#         f"Enter object type: 1 - {PERSON_CLASSES.get(1).__name__}, "
#         f"2 - {PERSON_CLASSES.get(2).__name__}, 3 - {PERSON_CLASSES.get(3).__name__}\n>> ")
#     )
#     if selected_class_number not in PERSON_CLASSES:
#         print("Invalid number")
#         continue
#     else:
#         name = input("Enter name: ")
#         age = int(input("Enter age: "))
#         phone_number = input("phone number: ")
#         passport_seria_number = input("passport seria and number: ")
#         extra_data = get_extra_data()
#         if selected_class_number == 1:
#             teacher = PERSON_CLASSES.get(selected_class_number)(
#                 name, age, get_region(), phone_number, passport_seria_number, **extra_data
#             )
#             teachers.append(teacher)
#         elif selected_class_number == 2:
#             student = PERSON_CLASSES.get(selected_class_number)(
#                 name, age, get_region(), phone_number, passport_seria_number, **extra_data
#             )
#             students.append(student)
#         elif selected_class_number == 3:
#             staff_obj = PERSON_CLASSES.get(selected_class_number)(
#                 name, age, get_region(), phone_number, passport_seria_number, **extra_data
#             )
#             staff.append(staff_obj)
