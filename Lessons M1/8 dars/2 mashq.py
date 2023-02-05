#    2  Online internet do'konida mahsulot narxini hisoblashda logistik to'lov, kilogrami va tannarxidan
# foydalaniladi, bunda narx formulasi quyidagicha: total_price = price * (100 + logistic_charge *
# kilogram) / 100. Mahsulot logistik to'lovi, kilogarami va narxi kiritilganda umumiy narxini
# hisoblash uchun funksiya yarating

narx = int(input('narx kiriting: '))


def dok(narx):
    kg = 30000
    logistic = 45000
    tannarx = 15000
    if narx > 30000:
        kg = 60000
    total_logistic_price = (tannarx + narx + kg + logistic)

    print(f"sizni narsangiz = {total_logistic_price} so'm boldi ")

dok(narx)