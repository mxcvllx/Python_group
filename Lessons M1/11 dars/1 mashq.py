""""""
"""
1. Berilgan dict key larini o’sish tartibida qaytaring.
squares = {8: 64, 1: 1, 3: 4, 5: 25}
# Output [1, 3 ,5, 8]
"""


def dictionary():
    key_value = {8: 64, 1: 1, 3: 4, 5: 25}

    print("key_value", key_value)

    for i in sorted(key_value.keys()):
        print(i, end=" ")


if __name__ == "__main__":
    dictionary()
