""""""
"""
12. Tuple lar dan iborat ro’yxat berilgan. Ushbu ro’yxatdan bo’sh tuple bo’lsa o’chirish uchun 2 xil
yechim keltiring.
"""







# def Remove(tuples):
# 	tuples = [t for t in tuples if t]
# 	return tuples
#
# tuples = [(), (1, 2, 3), (), ('hello', 'n', ''), ()]
# print(Remove(tuples))




def Remove(tuples):
	for i in tuples:
		if(i==()):
			tuples.remove(i)
	return tuples


tuples = [(), (1, 2, 3), (), ('hello', 'n', ''), ()]
print(Remove(tuples))






