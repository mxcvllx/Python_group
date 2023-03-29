def function():
    for j in range(1, 22):
        if j % 2 == 0:
            yield -j
        else:
            yield j


my_generator = iter(function())

print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
