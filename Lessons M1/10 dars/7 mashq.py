""""""
"""
 7. Berilgan tuple lardan iborat ro’yxatda tuple elementlari orasida manfiy 
sonlar bo’lsa tuple olib tashlang.
 """




test_list = [5, 6, -3, -8, 9, 11, -12, 2]


res = [ele for ele in test_list if ele > 0]

print("удаление отрицательные чисел : " + str(res))
