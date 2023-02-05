""""""
""" 
 17. 2 ta setda ham bor elementlarni qaytaring.
set1 = {10, 20, 30, 40, 50}
set2 = {50, 70, 80, 90, 10}
Output: {50, 10}

 """



def common_member(a, b):
    a_set = set(a)
    b_set = set(b)

    if (a_set & b_set):
        print(a_set & b_set)
    else:
        print("нету одинаковых элементвов")


a = {10, 20, 30, 40, 50}
b =  {50, 70, 80, 90, 10}

common_member(a, b)