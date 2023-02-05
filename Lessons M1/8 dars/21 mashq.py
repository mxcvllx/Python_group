""""""
"""
21. Quyidagi ko'rinishda qiymat qaytaruvchi funksiya yarating:
Input: Terminal
Output: 'Trmnl'
"""

def anti_vowel(text):
   text = list(text)
   for i in text[::-1]:
       if i in 'aeiouAEIOU':
          text.remove(i)
   return str(''.join(text))


print(anti_vowel('Terminal'))