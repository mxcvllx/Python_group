#8. Kiritilgan matnda nechta harf 2 martadan takrorlanganini hisoblovchi funksiya yarating



def countWords(stri, n):
    m = dict()
    for i in range(n):
        m[stri[i]] = m.get(stri[i] ,0) + 1

    res = 0
    for i in m.values():
        if i == 2:
            res += 1

    return res

# Driver code
s = input("введите строку: ")
n = len(s)
print(countWords(s, n))

