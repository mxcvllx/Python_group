""""""
"""my dict = "a = {"foo": 123, "bar": 456, "baz": 789}"
Quyidagi ko'rinishda dastur tuzind 
foo -> 123
bar -> 456
baz -> 789
"""
my_dict = {"foo": 123, "bar": 456, "baz": 789}
for key in my_dict:
    print(key, '->', my_dict[key])
