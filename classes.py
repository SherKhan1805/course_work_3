import datetime

class Operations:
    def __init__(self, data, amount, currency, description, to_, from_):
        self.data = data
        self.amount = amount
        self.currency = currency
        self.description = description
        self.to_ = to_
        self.from_ = from_

    # def __repr__(self):
    #     return

    def get_data(self):
        """
        Получает дату.
        Конвертирует ее в нормальный вид.
        """
        str_data = str(self.data)
        str_data = str_data[:8]
        return str_data



    def get_amount(self):
        """
        Получает количество денег при операции.
        """
        return self.amount

    def get_currency(self):
        """
        Получает наименование валюты.
        """
        return self.currency

    def get_description(self):
        """
        Получает описание операции.
        """
        return self.description

    def get_to_(self):
        """
        Получает информацию куда произошел перевод.
        """
        return self.to_

    def get_from_(self):
        """
        Получает информацию откуда произошел перевод.
        """
        return self.from_

