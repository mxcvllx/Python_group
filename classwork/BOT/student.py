class Student:
    def __init__(self, chat_id, fullname):
        self.chat_id = chat_id
        self.fullname = fullname

    def get_attrs_for_csv_writer(self):
        return {
            "chat_id": self.chat_id,
            "full_name": self.fullname
        }
