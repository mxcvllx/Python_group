#11. Kiritilgan so'z palindrom yoki palindrom emasligini funksiya orqali qaytaring.


def isPalindrome(str):

    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True


s = input('son kiriting va dastur palindromlikka tekshiradi: ')
ans = isPalindrome(s)

if (ans):
    print("Yes")
else:
    print("No")
