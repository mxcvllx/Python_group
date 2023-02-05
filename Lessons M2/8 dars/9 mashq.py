""""""
"""hariflar orasiga '#' belgisini joylaydigan funksiya """


def count_hash():
    file = open("task9.txt", "r")
    data = file.read()
    for letter in data:
        print(letter, end="#")

    file.close()


count_hash()
