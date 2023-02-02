def get_next_prime():
    a = 2
    while True:
        for j in range(2, a):
            if a % j == 0:
                break
        else:
            yield a
        a += 1


generator = get_next_prime()

for i in range(1, 169):
    print(next(generator))
