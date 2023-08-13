import datetime


class Operations:
    def __init__(self, date, amount, currency, description, to_, from_):
        self.date = date
        self.amount = amount
        self.currency = currency
        self.description = description
        self.from_ = from_
        self.to_ = to_


    def get_data(self):
        """
        Получает дату.
        Конвертирует ее в нормальный вид.
        """

        str_data = str(self.date)
        str_data = str_data[:8]
        date = datetime.datetime.strptime(str_data, '%Y%m%d')
        return date.strftime('%d.%m.%Y')

    def get_description(self):
        return self.description

    def get_from_(self):
        return self.from_

    def get_to_(self):
        return self.to_

    def get_amount(self):
        return f'{self.amount} {self.currency}'

