

#10. Kiritilgan so'zni uzunligini 4 xil ususlda hisoblang


a = 'hello world'

print(len(a))



def findLen(str):
    counter = 0
    for i in str:
        counter += 1
    return counter
str = "hello world"
print(findLen(str))




def findLen(str):
    counter = 0
    while str[counter:]:
        counter += 1
    return counter

str = "hello world"
print(findLen(str))



def findLen(str):
    if not str:
        return 0
    else:
        some_random_str = 'py'
        return ((some_random_str).join(str)).count(some_random_str) + 1
str = "hello world"
print(findLen(str))
