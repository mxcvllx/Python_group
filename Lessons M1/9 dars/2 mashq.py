""""""
"""
2. Berilgan ro’yxatdan ma’lum 2 ta indeksdagi elementlarini almashtiring.
"""


# def swapPositions(list, pos1, pos2):
#     list[pos1], list[pos2] = list[pos2], list[pos1]
#     return list
#
#
# List = [23, 65, 19, 90]
# pos1, pos2 = 1, 3
#
# print(swapPositions(List, pos1 - 1, pos2 - 1))




def swapPositions(list, pos1, pos2):
    first_ele = list.pop(pos1)
    second_ele = list.pop(pos2 - 1)

    list.insert(pos1, second_ele)
    list.insert(pos2, first_ele)

    return list


List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(swapPositions(List, pos1 - 1, pos2 - 1))
