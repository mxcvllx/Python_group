""""""
"""6. Berilgan list ni teskari ko’rinishga keltirish uchun 3 xil yechim keltiring."""






a = 'qwertyu'

print(a[::-1])




def reversed(variable):
    res=''
    for i in range(len(variable)-1,-1,-1):
        res+=variable[i]
    return res

n = reversed(input())
print(n)






def reversed1(variable):
    res=[]
    for i in range(len(variable)-1,-1,-1):
        res.append(variable[i])
    res=''.join(res)
    return res

n = reversed1(input())
print(n)
