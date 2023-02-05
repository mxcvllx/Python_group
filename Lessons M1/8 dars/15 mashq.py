#15. Berilgan matnda nuqta(.) bilan vergul(,) ni almashtiruvchi funksiya yarating



def Replace(str1):
    str1 = str1.replace(', ', 'third')
    str1 = str1.replace('.', ', ')
    str1 = str1.replace('third', '.')
    return str1

string = input("данно строка которя содержит в себе точки и запятые: ")
print(Replace(string))
