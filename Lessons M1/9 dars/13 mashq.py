""""""
"""
13. 12-masaladagi kabi berilgan listda bo’sh tuple emas bo’sh list larni 2 xil usulda o’chiring.
"""



# test_list = [(), (1, 2, 3), (), ('hello', 'n', ''), ()]
#
#
#
# res = list(filter(None, test_list))
#
# print(str(res))






def empty_list_remove(input_list):
	new_list = []
	for ele in input_list:
		if ele:
			new_list.append(ele)
	return new_list


input_list = [(), (1, 2, 3), (), ('hello', 'n', ''), ()]


print(f"Список после удаления пустого списка : {empty_list_remove(input_list)}")
