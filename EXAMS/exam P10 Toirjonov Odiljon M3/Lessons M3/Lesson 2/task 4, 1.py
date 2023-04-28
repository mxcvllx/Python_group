def only_even_parameters(dec_func):
    def little_func(a, b):
        for i in range(1, 3):
            if a % 2 == 0:
                if b % 2 == 0:
                    return dec_func(a, b)
                else:
                    return "Please add only even numbers!"
            else:
                return "Please add only even numbers!"

    return little_func


@only_even_parameters
def add(a, b):
    return a + b


print(add(2, 8))
print(add(1, 4))
