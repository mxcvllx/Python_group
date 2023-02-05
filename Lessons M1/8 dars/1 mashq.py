""""""

"""
1       Yandex taxi har bir xizmati uchun 15% xizmat haqi va 2% soliq uchun oladi, Haydovchi bir kunda
n so'm yandex taxi xizmati uchun haq to'ladi, haydovchining bir kunlik foydasini topuvchi
funksiya yarating.
"""


n = int(input('1 kunlik haydovchi tolovi: '))


def yandeks(n):
    procent = 2
    procent2 = 15
    oylik2 = n / 100 * procent2
    oylik = n / 100 * procent
    print(f"tozza oylik = {oylik2} soliq  = {oylik}")

yandeks(n)