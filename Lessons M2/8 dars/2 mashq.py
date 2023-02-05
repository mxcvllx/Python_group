""""""
"""t bilan boshlanmaydigan qatorlarni sanaydigan funksiya"""


def line_count():
    file = open("task2.txt", "r")
    count = 0
    for line in file:
        if line[0] not in 'T':
            count += 1
    file.close()
    print(f"'T' Bilan boshlanmaydigan qatorlar soni = {count} ga teng")


line_count()
