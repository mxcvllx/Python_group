""""""
"""
1 - Althought that wat may not be obvious at first unless you're Dutch,
berilgan string da 'a' harifi kelsa ularni indeksini a;lohidda listda qaytaring
"""

a = list("Although that way may not be obvious at first unless you're Dutch.")
d = []
for i in a:
    if i == 'a':
        d.append(i)
print(d)

