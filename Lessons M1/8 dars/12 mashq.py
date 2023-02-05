

#12. Kiritilgan matndan unli harflarni indexi bilan qaytaruvchi funksiya yarating




test_str = input(":")

print("оригинальный стринг= " + test_str)


res = []
vow=[97,101,105,111,117]
for ele in range(len(test_str)):
	if ord(test_str[ele]) in vow:
		res.append(ele)

print("вывод : " + str(res))
