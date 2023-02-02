def get_next_multiple(a):
    while True:
        yield a
        a += 2


b = 2
number = get_next_multiple(b)
print(next(number))
print(next(number))
print(next(number))
print(next(number))
