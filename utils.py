import json
import requests
import datetime
from operator import itemgetter
from classes import Operations


def unpacking_json():

    """
    Cортируем json-файл.
    Возвращает только успешные операции.
    """

    executed_list = []

    file = open("operations.json", encoding='utf-8')
    list_json = json.load(file)
    for operations in list_json:
        if operations.get("state") == "EXECUTED":
           executed_list.append(operations)
        else:
            continue

    """
    Получаем дату операции. Именяем ее формат.
    Меняем значение в словаре по ключу.
    """

    executed_list_2 = []

    for executed_operation in executed_list:

        date = datetime.datetime.strptime(executed_operation.get("date"), '%Y-%m-%dT%H:%M:%S.%f')
        new_date = f'{date:%Y%m%d%H%M%S%f}'
        executed_operation["date"] = int(new_date)
        executed_list_2.append(executed_operation)
        # print(new_date)
        # print(executed_operation)

    # print(executed_list_2)

    executed_list_3 = sorted(executed_list_2, key=itemgetter("date"))
    # print(executed_list_3)
    last_5_operation = executed_list_3[-5:]
    print(last_5_operation)

    last_5_operation = executed_list_3[-5:]
    for oper in last_5_operation:
        date = oper["date"]
        amount = oper["operationAmount"]["amount"]
        currency = oper["operationAmount"]["currency"]["name"]
        description = oper["description"]
        # from_ = oper["from"]                      """assert"""
        to_ = oper["to"]

        operations = Operations(date, amount, currency, description, to_)

        print(operations)

    # return list_json

unpacking_json()





