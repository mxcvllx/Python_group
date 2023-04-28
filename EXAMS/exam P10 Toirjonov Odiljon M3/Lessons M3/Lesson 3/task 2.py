with open("test.txt", "r+") as f:
    a = f.read()


def function():
    for i in a:
        yield i


my_generator = function()

print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
