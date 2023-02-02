import csv


class Work_Files:
    def __init__(self, file_1, file_2):
        self.file1 = file_1
        self.file2 = file_2

    @staticmethod
    def read_file(file):
        try:
            with open(file) as f:
                csv_read = csv.DictReader(f)
                return [row for row in csv_read]
        except FileNotFoundError as e:
            pass

    @staticmethod
    def make_csv_file(file_path, header, data):
        try:
            with open(file_path, 'w', encoding='utf8') as f:
                csv_writer = csv.DictWriter(f, header)
                csv_writer.writeheader()
                csv_writer.writerows(data)
        except FileNotFoundError:
            pass

    @staticmethod
    def format_date(date):
        """
        data format -> yyyy-mm-ddThh:mm:ssZ
        return data -> year month date
        """
        month = {
            1: 'January',
            2: 'February',
            3: 'March',
            4: 'April',
            5: 'May',
            6: 'June',
            7: 'July',
            8: 'August',
            9: 'September',
            10: 'October',
            11: 'November',
            12: 'December'
        }
        date = date.split('T')
        date_year = date[0][:4]
        date_month = month.get(int(date[0][5:7]))
        date_day = date[0][8:]
        res = f'{date_year} {date_month} {date_day}'
        return res

    def make_data(self, file_path_):
        first_file_data = self.read_file(self.file1)
        second_file_data = self.read_file(self.file2)
        result_data = []
        data = {}

        for row in second_file_data:

            f = row.get('Department_ID')
            for row_2 in first_file_data:
                department_id = row_2.get('Department_ID')
                if department_id == f:
                    id = row_2.get("Department_Name")
                    row.pop('Department_ID')
                    data = row.copy()
                    data['Department_Name'] = id
                    date_of_doj = self.format_date(data.get('DOJ'))
                    date_of_dob = self.format_date(data.get('DOJ'))
                    data['DOB'] = date_of_dob
                    data['DOJ'] = date_of_doj
                    result_data.append(data)

        header = result_data[0].keys()
        self.make_csv_file(file_path_, header, result_data)


file_path = 'csv_files/Employee_Department.csv'
file_1_path = 'csv_files/Department_information.csv'
file_2_path = 'csv_files/Employee_information.csv'
file_obj = Work_Files(file_1_path, file_2_path)