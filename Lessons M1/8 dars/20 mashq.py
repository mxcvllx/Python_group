""""""


"""
20. Quyidagi ko'rinishda qiymat qaytaruvchi funksiya yarating:
Input: Terminal
Output: ['T', 'rm', 'n', 'l']
"""

s = 'T rm n l'

i = 0
while s[i] == ' ':
    i += 1
s = s[i:]

i = len(s)
while s[i - 1] == ' ':
    i -= 1
s = s[:i]

s_new = s[0]
i = 1
while i < len(s):
    if s[i] != ' ':
        s_new += s[i]
    elif s[i - 1] != ' ':
        s_new += "' '"
    i += 1
print(s_new + '!')