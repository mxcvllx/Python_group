import csv
import os.path
import tkinter as tk
from datetime import datetime

from task import Task
from message import TASK_NAME_LABEL, ADD_BTN

window = tk.Tk()
window.title("Todo application")

width, height = 500, 500
window.geometry(f"{width}x{height}")

file_path = "tasks.csv"


def get_prev_task_id():
    with open(file_path) as f:
        csv_reader = csv.DictReader(f)
        return int([row for row in csv_reader][-1].get("id"))


def get_tasks():
    with open(file_path) as f:
        csv_reader = csv.DictReader(f)
        data = [list(row.values()) for row in csv_reader]
        for i in range(0, len(data)):
            for j in range(4):
                row = tk.Label(window, text=data[i][j])
                row.grid(row=i + 1, sticky='w', column=j, pady=2)


def add():
    task = Task(name=task_entry.get(), created_at=datetime.now())

    with open(file_path, "a+", newline="\n") as f:
        data = task.get_attrs_as_dict()
        header = ["id", "name", "created_at", "updated_at"]
        dict_writer = csv.DictWriter(f, header)
        if os.path.getsize(file_path) == 0:
            dict_writer.writeheader()
            data.update({"id": 1})
        data.update({"id": get_prev_task_id() + 1})
        dict_writer.writerow(data)

    task_entry.delete(0, tk.END)

    get_tasks()


task_name = tk.Label(window, text=TASK_NAME_LABEL)
task_name.grid(row=0, column=0)

task_entry = tk.Entry(window, width=15)
task_entry.grid(row=0, column=1)

add_btn = tk.Button(text=ADD_BTN, command=add)
add_btn.grid(row=0, column=2)

# with open(file_path)

if __name__ == "__main__":
    window.mainloop()
