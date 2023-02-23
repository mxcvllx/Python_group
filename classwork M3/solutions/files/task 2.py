def get_population_gt_20m():
    """
    Population greater than or equal 20M
    """
    result = []

    with open("../../csv/countries of the world.csv") as f:
        lines = f.readlines()

    for line in lines[1:]:
        try:
            name, count = line.split(",")[0].strip(), int(line.split(",")[2].strip())
        except ValueError as e:
            print(e)
        else:
            if count > 20000000:
                result.append(f"{name}: {count}")

    return result


print(get_population_gt_20m())
