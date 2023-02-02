""""""
"""4 dan uzun sozlarni qaytaradigan funksiya"""


def display_words():
    try:
        file = open("tashtfk5.txt", "r")
    except FileNotFoundError as err:
        print(err)
    else:
        data = file.read()
        words = data.split()
        for word in words:
            if len(word) < 4:
                print(word, end=" ")
        file.close()


display_words()
