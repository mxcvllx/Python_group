class Save:
    def __init__(self, first_name, last_name, phone, age, language, course):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.age = age
        self.language = language
        self.course = course

    def get_save_func(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone': self.phone,
            'age': self.age,
            'language': self.language,
            'course': self.course
        }