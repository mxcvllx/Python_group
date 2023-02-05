""""""
"""
3. Berilgan list elementlar yig’indisini 2 xil usulda hisoblang.
"""

# total = 0
# list1 = [11, 5, 17, 18, 23]
#
#
# for ele in range(0, len(list1)):
# 	total = total + list1[ele]
#
# print("сумма ваших элементов: ", total)

#///////////////////////////////////////

total = 0
ele = 0

list1 = [11, 5, 17, 18, 23]


while (ele < len(list1)):
    total = total + list1[ele]
    ele += 1

print("сумма ваших элементов: ", total)