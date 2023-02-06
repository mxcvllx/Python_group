import tkinter as tk
import csv
import os
from tkinter import messagebox

window = tk.Tk()
window.title("Регистрация")
window.geometry("600x600")

reg = []


def show_message():
    messagebox.showinfo("Payment", f"Your payment {reg[-1].get('Payment')}")


def registration():
    info = {
        "Fullname": fullname_entry.get(),
        "Age": age_entry.get(),
        "Address": address_entry.get(),
        "Days": days_entry.get(),
        "Payment": f"{int(days_entry.get()) * 300}$"
    }
    reg.append(info)
    header = ["Fullname", "Age", "Address", "Days", "Payment"]
    try:
        with open("registrations.csv", "a") as f:
            f = csv.DictWriter(f, header)
            if os.path.getsize("registrations.csv") == 0:
                f.writeheader()
            f.writerows(reg)
    except FileNotFoundError as e:
        return f"{e} FileNotFoundError"
    else:
        show_message()


# Full name
fullname_label = tk.Label(window, text="Введите полное имя: ")
fullname_label.grid(column=0, row=0)
fullname_entry = tk.Entry(window)
fullname_entry.grid(column=1, row=0)

# Age
age_label = tk.Label(window, text="Введите возраст: ")
age_label.grid(column=0, row=1)
age_entry = tk.Entry(window)
age_entry.grid(column=1, row=1)

# Address
address_label = tk.Label(window, text="Введиет адресс: ")
address_label.grid(column=0, row=3)
address_entry = tk.Entry(window)
address_entry.grid(column=1, row=3)

# Days
days_label = tk.Label(window, text="на сколько дней хотите забронировать: ")
days_label.grid(column=0, row=4)
days_entry = tk.Entry(window)
days_entry.grid(column=1, row=4)

# Price
price_label = tk.Label(window, text="Один день стоит 300$")
price_label.grid(column=1, row=5)

# Button registration
reg_btn = tk.Button(window, text="Registration", command=registration)
reg_btn.grid(column=0, row=5)

window.mainloop()
