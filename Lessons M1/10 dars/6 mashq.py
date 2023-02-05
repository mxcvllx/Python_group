""""""
""" 
6. Berilgan tuple lardan iborat ro’yxatda tuple elementlari 6 ga 
bo’linmaydigan sonlar bo’lsa tuple olib tashlang.
 """






test_list = [(6, 24, 12), (60, 12, 6), (12, 18, 21)]





K = 6


res = [sub for sub in test_list if all(ele % K == 0 for ele in sub)]


print("вывод: " + str(res))
