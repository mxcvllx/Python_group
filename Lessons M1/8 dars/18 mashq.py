""""""

"""
18. Probel bilan ajratilgan so'zlarni snake_case, camelCase, PascalCase, kebab-case ga o'tkazuvchi
funksiya yarating
"""
s = input()

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
        s_new += "_"
    i += 1
print(s_new + '!')