""""""
"""'e' bilan tugaydigan sozlarni sanaydigan funksiya"""


def count_words():
    file = open("task7.txt", "r")
    count = 0
    data = file.read()
    words = data.split()
    for word in words:
        if word[-1] == 'e':
            count += 1
    print(f"'e' blan tugidigan sozlar = {count} ga teng")
    file.close()


count_words()
