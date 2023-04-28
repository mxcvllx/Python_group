""""""
"""
3 - lst = ['apple', 'banana', 'peach', 42], listda string tipidagi har bir elementlardan yonida oxiridagi
raqami birga qaytaring 
"""

lst = ['apple', 'banana', 'peach', 42]
r = lst.pop(-1)
for i in lst:
    print(i, r)