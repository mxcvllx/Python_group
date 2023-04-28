def main_func(dec_func):
    def little_func(lst):
        if type(dec_func(lst)) != list:
            return "Please send only list."
        else:
            return dec_func(lst)

    return little_func


@main_func
def sum_index(lst):
    typ = lst
    result = 0
    for i in range(0, len(lst)):
        result = result + i
    return typ


print(sum_index([2, 4, 5, 6]))
print(sum_index((2, 4, 5, 6)))

