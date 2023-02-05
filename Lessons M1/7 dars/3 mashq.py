#3. n ta talaba uchun umumiy k ta olma mavjud. Har bir talabaga bir xil miqdorda olma tarqatilsa qancha olma ortib
# qolishini aniqlovchi funksiya yarating.



def leftover(apples, kids):
    if apples >= kids:
        return apples % kids
    return 'Not enough apples!'


apples = int(input('Enter the number of apples: '))
kids = int(input('Enter the number of kids: '))
print(leftover(apples, kids))
