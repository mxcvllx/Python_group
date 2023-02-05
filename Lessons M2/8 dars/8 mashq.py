""""""
"""katta hariflarni sanaydigan funfsiya"""


def count_letter():
    file = open("task8.txt", "r")
    data = file.read()
    count = 0
    for letter in data:
        if letter.isupper():
            count += 1
    print(f"kotta hariflar soni = {count} ga teng")
    file.close()


count_letter()
