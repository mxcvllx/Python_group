import csv
import os


def write_to_csv(student):
    with open("students.csv", "a+", newline="\n") as f:
        header = ["chat_id", "fullname"]
        csv_writer = csv.DictWriter(f, header)
        if os.path.getsize("students.csv") == 0:
            csv_writer.writeheader()
        csv_writer.writerow(student.get_attrs_for_csv_writer())
    print("Student add succesfully.")


def is_exist_chat_id(chat_id):
    with open("students.csv") as f:
        csv_reader = csv.DictReader(f)
        return chat_id in [row.get("chat_id") for row in csv_reader]
