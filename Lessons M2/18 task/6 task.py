""""""
"""this these sizlarini sanaydigan funfsiya"""


def count_words():
    file = open("task6.txt", "r")
    count = 0
    data = file.read()
    words = data.split()
    for word in words:
        if word == 'this' or word == 'these':
            count += 1
    print(f"'this' 'these' sozlari = {count} ta")
    file.close()


count_words()
