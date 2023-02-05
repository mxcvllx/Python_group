""""""
"""
	2. Berilgan dict value larini alifbo A-Z tartibida qaytaring.
"""





dict = {"uz": "Uzbek", "ru": "Russian", "en" : "English"}


print("\nBefore Sorting: ")
for x in dict.items():
	print(x)

print("\nAfter Sorting: ")
for i, j in dict.items():
	sorted_dict ={i:sorted(j)}
	print(sorted_dict)

