""""""
"""
6. Berilgan dictda key bor yoki yo'qligi tekshiring.
"""


def checkKey(dic, key):
    if key in dic.keys():
        print("Present, ", end=" ")
        print("value =", dic[key])
    else:
        print("нету ключа")


dic = {"id": 123, "name": "Aaa", "age": 20}
key = 'b'
checkKey(dic, key)

key = 'id'
checkKey(dic, key)
