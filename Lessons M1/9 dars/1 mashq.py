""""""

"""
1. Berilgan ro’yxatdan birinchi va oxirgi elementlarini almashtiring.
"""


lst = [1, 4, 5, 7]
Output: [7, 4, 5, 1]


def swapList(newList):
    size = len(newList)

    # Swapping
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp

    return newList


newList =  [1, 4, 5, 7]


print(swapList(newList))