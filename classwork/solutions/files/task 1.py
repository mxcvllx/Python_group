# "countries of the world.csv" file da berilgan ma'lumotlar
# orqali quyidagi ma'lumotlarni chiqaring.
# a) Population 20 000 000 dan ko'p bo'lgan mamlakatlar ro'yxatini chiqaring.
# b) C bilan boshlanadigan davlatlar ro'yxatini txt file ga yozing.
# c) GDP 1000 dan baland bo'lganlar ro'yxatini qaytaring.

from solutions.utils import get_countries_data


def get_population_gt_20m():
    """
    Population greater than or equal 20M
    """
    result = []

    file_path = "../../csv/countries of the world.csv"

    for line in get_countries_data(file_path)[1:]:  # noqa
        name, count = line[0].strip(), int(line[2].strip())
        if count > 20000000:
            result.append(f"{name}: {count}")

    return result


# def get_countries_with_c():
#     for line in get_countries_data():
#         print(line)
#     result = [
#         line.split(",")[0].strip()
#         for line in get_countries_data[1:]
#         if line.split(",")[0].strip().startswith("C")
#     ]
#
#     return result


print(get_population_gt_20m())
