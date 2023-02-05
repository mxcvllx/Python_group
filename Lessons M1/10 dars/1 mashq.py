""""""
""" 
Berilgan tuple tpl = ("A", 1, "B", 2, "C", 3) uzunligini ikki xil usulda 
hisoblang.
 """

tpl = ("A", 1, "B", 2, "C", 3)

def lenn(tpl):
    print(len(tpl))
    print(type(tpl))

lenn(tpl)




def findLen(str):
    counter = 0
    for i in str:
        counter += 1
    return counter
str = ("A", 1, "B", 2, "C", 3)
print(findLen(str))
