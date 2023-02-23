import tkinter as tk

window = tk.Tk()
window.title("P10 TEST")
width = 600
height = 600
window.geometry(f"{width}x{height}")

name_Lable = tk.Label(window, text="Full name: ")
name_Lable.place(x=165, y=10)

name_entry = tk.Entry(window, width=20)
name_entry.place(x=250, y=10)

name_email = tk.Label(window, text="Email: ")
name_email.place(x=165, y=40)

name_email = tk.Entry(window, width=20)
name_email.place(x=250, y=40)

name_Dop = tk.Label(window, text="Dop: ")
name_Dop.place(x=165, y=80)

name_Dop = tk.Entry(window, width=20)
name_Dop.place(x=250, y=80)

name_Gender = tk.Label(window, text="Gender: ")
name_Gender.place(x=165, y=110)

name_Gender = tk.Entry(window, width=20)
name_Gender.place(x=250, y=110)

name_Phone = tk.Label(window, text="Phone: ")
name_Phone.place(x=165, y=140)

name_Phone = tk.Entry(window, width=20)
name_Phone.place(x=250, y=140)

name_Course = tk.Label(window, text="Course: ")
name_Course.place(x=165, y=170)

name_Course = tk.Entry(window, width=20)
name_Course.place(x=250, y=170)

save_btn = tk.Button(text="save")
save_btn.place(x=200, y=210)

save_add = tk.Button(text="add")
save_add.place(x=250, y=210)

save_clear = tk.Button(text="clear")
save_clear.place(x=300, y=210)

save_exit = tk.Button(text="Exit", command=window.quit  )
save_exit.place(x=350, y=210)

if __name__ == "__main__":
    window.mainloop()
