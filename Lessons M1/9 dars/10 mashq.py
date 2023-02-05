""""""

"""10. Berilgan listda manfiy va musbat sonlar sonini qaytaring.
"""

list1 = [10, -21, 4, -45, 66, -93, 1]

pos_count, neg_count = 0, 0

for num in list1:

	if num >= 0:
		pos_count += 1

	else:
		neg_count += 1

print("Musbat: ", pos_count)
print("Manfiy: ", neg_count)
