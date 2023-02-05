#7. Kiritilgan Ikkita raqam orasida nechta juft son borligini aniqlaydigan funksiya yarating.

num1 = int(input("enter num1"))
num2 = int(input("enter num2"))

def even(num1,num2):
    if num1>num2:
        return
    print(num1,end=" ")
    return even(num1+2,num2)

even(num1,num2)
