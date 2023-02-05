""""""
"""
8. Mahsulotlar nomi va narxidan iborat ro'yxat mavjud, umumiy narxni qaytaring.
"""



def returnSum(myDict):

	list = []
	for i in myDict:
		list.append(myDict[i])
	final = sum(list)

	return final


dict = {"Apple": 5000, "Strawberry": 7000, "Cherry": 6000}
print("Sum :", returnSum(dict))
