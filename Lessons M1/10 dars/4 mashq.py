""""""
"""
4. Berilgan 2 ta tupleda tuzish mumkin bo’lgan barcha tuple kombinatsiyalarni listda qaytaring
"""


test_tuple1 = ([7, 2])
test_tuple2 = ([7, 8])




res = [(a, b) for a in test_tuple1 for b in test_tuple2]
res = res + [(a, b) for a in test_tuple2 for b in test_tuple1]

print("output: " + str(res))
