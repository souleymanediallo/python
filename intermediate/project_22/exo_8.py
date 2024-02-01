class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def arrange_value_into_date_pattern(self):
        date = str(self.day) + '-' + str(self.month) + '-' + str(self.year)
        return date

    @classmethod
    def get_data_form_string(cls, string):
        import re
        data = re.findall('\d{2}-\d{2}-\d{4}|\d{2}/\d{2}/\d{4}', string)[0]  # 17/06/2022
        list_date = data.replace('/', '-').split('-')
        print(list_date)
        day = list_date[0]
        month = list_date[1]
        year = list_date[2]
        return cls(year, month, day)

    @staticmethod  # 2024-01-01 ---> 01-062-2024
    def set_date_pattern(string):
        list1 = string.replace('/', '-').split('-')
        print(list1)
        date_update = list1[2] + '-' + list1[1] + '-' + list1[0]
        return date_update