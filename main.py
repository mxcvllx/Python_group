import tkinter as tk
from translate import Translator
import csv
from datetime import datetime
from trans_obj import Trans
import os



root = tk.Tk()
root.title("Translator")
root.geometry('550x500')
root.configure(bg='#82CAFA')


trans = [" "]

def history():
    task = Trans(f"{entry.get()} - {trans[0]}", datetime.now())

    with open('history.csv', "a", newline="\n") as f:
        data = task.get_attrs()
        header = ["Trans_word", "DOJ"]
        dict_writer = csv.DictWriter(f, header)
        if os.path.getsize('history.csv') == 0:
            dict_writer.writeheader()
        dict_writer.writerow(data)





def translate_word():

    translator = Translator(to_lang="uz")
    word = entry.get()
    translation = translator.translate(word)
    del trans[0]
    trans.append(translation)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, translation)

    history()

label = tk.Label(text="Kirit>")
label.place(x=10, y=20)
label.configure(font=1, bg='#82CAFA')

entry = tk.Entry(root)
entry.place(x=80, y=20)
entry.configure(font=1, width=30, border=5)

translate_button = tk.Button(root, text="Translate", command=translate_word)
translate_button.place(x=120, y=70)
translate_button.configure(font=1, border=5, activebackground="blue")

result_text = tk.Text(root)
result_text.place(x=0, y=125)
result_text.configure(font=1)

root.mainloop()
