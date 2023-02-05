""""""
"""
9. Berilgan listda eng katta, va eng kichik elementlarini 2 xi usulda min() va max() built-in
funksiyalarsiz qaytaring
"""


lst = [54, 982, 36, 2, 24, 5435432]


print('максимальное число: ',max(lst),'минимальное число:', min(lst))




def large(arr):
    max_ = arr[0]
    for ele in arr:
        if ele > max_:
           max_ = ele
    return max_


list1 = [1,4,5,2,6]
result = large(list1)
print('максимальное значение:',result)














