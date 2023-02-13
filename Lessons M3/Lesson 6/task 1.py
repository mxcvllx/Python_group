import tkinter as tk
from datetime import date

window = tk.Tk()
window.title("Calculate age")
window.geometry("250x200")


def calculate():
    today = date.today()
    user_year = int(entry.get())
    if user_year <= 0 or user_year >= today.year:
        result_label["text"] = "Error"
    else:
        result_age = today.year - user_year
        result_label["text"] = result_age


label_1 = tk.Label(text="Birth year:", font=50)
label_1.place(x=20, y=10)

label_2 = tk.Label(text="Your age:", font=50)
label_2.place(x=20, y=70)

result_label = tk.Label(text="None", font=50)
result_label.place(x=110, y=70)

entry = tk.Entry(window)
entry.place(x=100, y=10)

button = tk.Button(window, text="Calculate", command=calculate, font=50)
button.place(x=90, y=110)

if __name__ == "__main__":
    window.mainloop()