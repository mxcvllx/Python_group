""""""
"""
8. Berilgan listda elementlarini uning raqamlar yig’indisiga almashtiring.
"""

test_list =  [12, 34, 56, 78]





res = []
for ele in test_list:
    sum = 0
    for digit in str(ele):
        sum += int(digit)
    res.append(sum)


print("сумма введённых цифр: " + str(res))
