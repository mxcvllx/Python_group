""""""
""" 3  Berilgan tuple da o’zidan keyingi kelgan element bilan ko’paytmasini 
alohida tupleda qaytaring.
 """


Input = [(2, 3),
         (4, 5),
         (6, 7),
         (2, 8)]

Output = []


for elem in Input:
	temp = elem[0]*elem[1]
	Output.append(temp)



print(Output)
