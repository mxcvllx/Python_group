import tkinter as tk
import csv
import os
from tkinter import messagebox

window = tk.Tk()
window.title("Registration")
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
        "Payment": f"{int(days_entry.get()) * 15}$"
    }
    reg.append(info)
    header = ["Fullname", "Age", "Address", "Days", "Payment"]
    try:
        with open("registrations.csv", "a") as f:
            f = csv.DictWriter(f, header)
            if os.path.getsize("registrations.csv")  == 0:
                f.writeheader()
            f.writerows(reg)
    except FileNotFoundError as e:
        return f"{e} FileNotFoundError"
    else:
        show_message()


# Full name
fullname_label = tk.Label(window, text="Enter full name: ")
fullname_label.grid(column=0, row=0)
fullname_entry = tk.Entry(window)
fullname_entry.grid(column=1, row=0)

# Age
age_label = tk.Label(window, text="Enter age: ")
age_label.grid(column=0, row=1)
age_entry = tk.Entry(window)
age_entry.grid(column=1, row=1)

# Address
address_label = tk.Label(window, text="Enter address: ")
address_label.grid(column=0, row=3)
address_entry = tk.Entry(window)
address_entry.grid(column=1, row=3)

# Days
days_label = tk.Label(window, text="How many days: ")
days_label.grid(column=0, row=4)
days_entry = tk.Entry(window)
days_entry.grid(column=1, row=4)

# Price
price_label = tk.Label(window, text="One days 15$")
price_label.grid(column=1, row=5)

# Button registration
reg_btn = tk.Button(window, text="Registration", command=registration)
reg_btn.grid(column=0, row=5)

window.mainloop()
