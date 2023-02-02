""""""
""" 'the" sozini sanaydigan funksiya """


def count_words():
    file = open("task4.txt", "r")
    count = 0
    data = file.read()
    words = data.split()
    for word in words:
        if word == "the" or word == "The":
            count += 1
    print(f"'the' sozi = {count} martta kaytarilgan")
    file.close()


count_words()
