class Student:
    def __init__(self, fullname, email, dob, gender, phone, course, doj):
        self.fullname = fullname
        self.email = email
        self.dob = dob
        self.gender = gender
        self.phone = phone
        self.course = course
        self.doj = doj

    def get_attrs(self, as_dict=False):
        if as_dict:
            return {
                "Fullname": self.fullname,
                "Email": self.email,
                "DOB": self.dob,
                "Gender": self.gender,
                "Phone": self.phone,
                "Course": self.course,
                "DOJ": self.doj
            }
        return [
            self.fullname,
            self.email,
            self.dob,
            self.gender,
            self.phone,
            self.course,
            self.doj
        ]