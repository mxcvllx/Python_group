""""""
"""
4. List comprehension orqali 1 dan 20 gacha sonlar orasida juft
sonlar yig’indisini hioblang.
"""

d = []
for i in range(1, 20):
    if i % 2 == 0:
        d.append(i)
print(d)
