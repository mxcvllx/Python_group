""""""
"""txt faylda nechta soz borligini sanaydigan funksiya"""


def count_words():
    file = open("task3.txt", "r")
    count = 0
    data = file.read()
    words = data.split()
    for word in words:
        count += 1
    print(f"Sozlar soni = {count} ga teng")
    file.close()


count_words()
