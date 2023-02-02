""""""
"""txt fayl oqiydigan funksiya"""


def read_file():
    file = open("task1.txt", "r")
    for line in file:
        print(line, end="")
    file.close()


read_file()
