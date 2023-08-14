from utils import unpacking_json

"""
Вывод на экран информации по 5 последним операциям в цикле в удобном для пользователя виде
"""
unpacking_json = unpacking_json()

user_input = input(f'Для вывода информации о последних {len(unpacking_json)} операциях нажмите Enter\n')
for operation in unpacking_json:
    print(operation)
