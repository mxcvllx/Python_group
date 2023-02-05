""""""
"""
14. Berign listda 1 marta takrorlangan elementlar sonini qaytaring.
"""



def countX(lst, x):
	count = 0
	for ele in lst:
		if (ele == x):
			count = count + 1
	return count


lst = [8, 6, 10, 20, 10]
x = 8
print('{} произошло {} раз'.format(x,countX(lst, x)))
