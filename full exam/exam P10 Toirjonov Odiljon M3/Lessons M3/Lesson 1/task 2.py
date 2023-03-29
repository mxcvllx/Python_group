from task_1 import Work_Files


class WorkWithFile(Work_Files):
    def __init__(self, file_1, file_2, instagram_csv_file):
        super().__init__(file_1, file_2)
        self.file = instagram_csv_file

    def display(self):
        data = self.read_file(self.file)
        [print(row) for row in data]

    def make_data_by_country_name(self):
        country_names_and_data = {}

        data = self.read_file(self.file)
        header = list(data[0].keys())
        for row in data:
            country_name = row.get('Country/Continent')

            if country_name not in list(country_names_and_data.keys()):
                country_names_and_data[country_name] = [row]
            else:
                country_names_and_data.get(country_name).append(row)

        for name, data_ in country_names_and_data.items():
            file_path = f'task_2.csv/accounts/{name} account.csv'

            self.make_csv_file(file_path, header, data_)


file_1_path = 'task_1.csv/Department_information.csv'
file_2_path = 'task_1.csv/Employee_information.csv'
instagram_csv_file_path = 'task_2.csv/list_of_most_followed_instagram_account.csv'

file_obj = WorkWithFile(file_1_path, file_2_path, instagram_csv_file_path)
