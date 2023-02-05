class Person:
    def __init__(self, name, surname, job, gender):
        self.name = name
        self.surname = surname
        self.job = job
        self.gender = gender

    def get_main_info(self):
        a = ""
        if self.gender == "male" or self.gender == "boy":
            return f"His name is {self.name}, his surname is {self.surname} and he is a {self.job}"
        elif self.gender == "female" or self.gender == "girl":
            return f"Her name is {self.name}, Her surname is {self.surname} and she is a {self.job}"


name = input("Enter name: ")
surname = input("Enter suraname: ")
job = input("Enter Job: ")
gender = input("Enter Gender: ")

person = Person(name, surname, job, gender)
print(person.get_main_info())
