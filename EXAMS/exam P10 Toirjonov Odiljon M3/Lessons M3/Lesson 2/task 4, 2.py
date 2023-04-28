def only_even_parametrs(dec_func):
    def little_func(*args):
        q = 0
        for i in args:
            if i % 2 == 0:
                q += 1
                continue
            else:
                return "Please enter multple only even numbers!"
        if q >= 4:
            return dec_func(*args)

    return little_func


@only_even_parametrs
def multiply(a, b, c, d, s):
    return a * b * c * d


print(multiply(2, 6, 4, 8))
print(multiply(1, 2, 2, 8))
