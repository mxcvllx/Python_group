
#3. Kiritilgan so'zning o'rtasidagi harfni qaytaruvchi funksiya yarating.

def middle_char(txt):
  return txt[(len(txt)-1)//2:(len(txt)+2)//2]

text = input('введите строку ')
print("оригинальная строка: ",text)
print("средний символ указонного слова: ",middle_char(text))
