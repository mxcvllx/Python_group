
#16. Kiritilgan matndan URL ni ajratuvchi funksiya yarating


test_str = 'www.youtube.com/?is = nice platform'

print("Исходная строка: " + str(test_str))

res = test_str[0:test_str.index('?')]

print("Базовый URL-адрес: " + res)
