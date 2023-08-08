import json
import requests
import datetime


def unpacking_json():

    """
    Функция сортирует json-файл.
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

    for executed_operation in executed_list:

        date = datetime.datetime.strptime(executed_operation.get("date"), '%Y-%m-%dT%H:%M:%S.%f')
        new_date = f'{date:%Y%m%d%H%M%S%f}'
        executed_operation["date"] = new_date
        print(new_date)
        print(executed_operation)

    # print(len(executed_operation))

    return list_json

print(unpacking_json())


# date = datetime.datetime.strptime('2019-08-26T10:50:58.294041', '%Y-%m-%dT%H:%M:%S.%f')
# print(f'{date:%d.%m.%Y}')
# 26.08.2019


