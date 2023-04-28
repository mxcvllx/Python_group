def add(a, b):
    def inner_func():
        return (a + b) * 2

    return inner_func


a = int(input("Enter the number of a ->"))
b = int(input("Enter the number of b ->"))

print(add(a, b))
