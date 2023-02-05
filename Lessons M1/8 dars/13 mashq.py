
#13. Kiritilgan 2 ta so'zdan bir xil harfalarni qaytaruvchi funksiya yarating.


from collections import Counter

def common(str1 ,str2):

    dict1 = Counter(str1)
    dict2 = Counter(str2)

    commonDict = dict1 & dict2

    if len(commonDict) == 0:
        print (-1)
        return

    commonChars = list(commonDict.elements())


    commonChars = sorted(commonChars)


    print (''.join(commonChars))

if __name__ == "__main__":
    str1 = 'pdp academy'
    str2 = ' academy'
    common(str1, str2)
