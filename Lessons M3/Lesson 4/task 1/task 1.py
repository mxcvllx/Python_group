from datetime import date
import tkinter as tk


window = tk.Tk()
window.title('Age detection software')
window.geometry('300x300')


def age_func():
    data = date.today()
    year = int(entry.get())
    if year <= 0 or year >= 2023:
        result['text'] = 'Error'
    else:
        age = data.year - year
        result['text'] = age


lab1 = tk.Label(text='year:')
lab1.place(x=40, y=10)

lab2 = tk.Label(text='age:')
lab2.place(x=40, y=50)

result = tk.Label(text="0")
result.place(x=80, y=50)

entry = tk.Entry(window)
entry.place(x=100, y=10)

button = tk.Button(window, text='find out how old', command=age_func)
button.place(x=105, y=75)

if __name__ == "__main__":
    window.mainloop()
