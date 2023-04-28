""""""
"""
3 - add_tags nomli funksiya yarating bunda funksiya 2 ta argument tag va string qabul qiladi
Natija html tag sifatida qaytaradi
"""


def add_tags(tag, word):
    return "<%s>%s</%s>" % (tag, word, tag)


print(add_tags("b", "Hello, Python"))
print(add_tags("h1", "Hello, Python"))
