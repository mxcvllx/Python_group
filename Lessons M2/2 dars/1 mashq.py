class Student():
    def __init__(self, full_name, age, subjects):
        self.full_name = full_name
        self.age = age
        self.subjects = subjects

    def get_info(self):
        print("Funksiya ishlayapti")
        info = f"Full name:{self.full_name}, Age: {self.age}" \
               f"Subjects: {[subject.get('name') for subject in subjects_data]}"
        return info

    def get_average_marks(self):
        marks_sum = self.get_marks_sum(self.subjects)
        subjects_count = self.get_subjects_count(self.subjects)
        return round(marks_sum / subjects_count, 2)

    @staticmethod
    def get_marks_sum(data):
        return sum(subject.get('mark') for subject in data)

    @staticmethod
    def get_subjects_count(data):
        return len(data)


subjects_data = [
    {"id": 1, "name": "math", "mark": 5},
    {"id": 2, "name": "Python", "mark": 4},
    {"id": 3, "name": "Pyhsics", "mark": 3},
    {"id": 4, "name": "C++", "mark": 5}

]

student = Student("A", 20, subjects_data)

print(student.get_info())
print(student.get_average_marks())