with open("planets.txt", "r+") as f:
    a = f.readlines()


def func():
    for i in range(0, len(a) + 1, 5):
        result = a[i].split("\n")[0][7:]
        yield result


my_func = iter(func())

print(next(my_func))
print(next(my_func))
print(next(my_func))
print(next(my_func))
