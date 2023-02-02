import csv


def get_countries_data(file_path):
    with open(file_path) as f:
        data = [[value.strip() for value in row] for row in csv.reader(f)]
    return data


print(get_countries_data("../solutions/custom_data.csv"))


def custom_csv_writer(file_path, columns, data):
    with open(file_path, "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(columns)
        csv_writer.writerows(data)


def custom_csv_writer_with_dict(file_path, columns, data):
    with open(file_path, "w") as f:
        csv_writer = csv.DictWriter(f, columns)
        csv_writer.writeheader()
        csv_writer.writerows(data)


header = ['Country', 'Region', 'Population', 'Area (sq. mi.)', 'GDP ($ per capita)']
data = [
    ['Afghanistan ', 'ASIA (EX. NEAR EAST)', '31056997', '647500', '700'],
    ['Albania ', 'EASTERN EUROPE                     ', '3581655', '28748', '4500'],
    ['Algeria ', 'NORTHERN AFRICA                    ', '32930091', '2381740', '6000'],
]

dict_header = ['name', 'area', 'country_code2', 'country_code3']

rows = [
    {
        'name': 'Albania',
        'area': 28748,
        'country_code2': 'AL',
        'country_code3': 'ALB'
    },
    {
        'name': 'Algeria',
        'area': 2381741,
        'country_code2': 'DZ',
        'country_code3': 'DZA'
    },
    {
        'name': 'American Samoa',
        'area': 199,
        'country_code2': 'AS',
        'country_code3': 'ASM'
    }
]

# custom_csv_writer("../solutions/custom_data.csv", header, data)
custom_csv_writer_with_dict("../solutions/custom_data.csv", dict_header, rows)
