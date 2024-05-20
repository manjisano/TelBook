from prettytable import PrettyTable

from working_with_file.read_file import read
from input import input_surname


def check_data():
    """Функция вывода базы данных"""

    # Настройка таблицы
    tab3 = PrettyTable(title='Список учащихся', border=True, header=True,
                       vertical_char='│',
                       horizontal_char='─',
                       junction_char='┼',
                       left_junction_char='├',
                       right_junction_char='┤',
                       top_left_junction_char='┌',
                       top_right_junction_char='┐',
                       top_junction_char='┬',
                       bottom_junction_char='┴',
                       bottom_right_junction_char='┘',
                       bottom_left_junction_char='└',
                       start=0,
                       )

    tab3.field_names = ['Фамилия', 'Имя', 'Отчество', 'Телефон']
    tab3.align['Фамилия'] = 'l'
    tab3.align['Имя'] = 'с'
    tab3.align['Отчество'] = 'с'
    tab3.align['Телефон'] = 'r'
    tab3.sortby = 'Фамилия'

    data = read()

    # Заполнение таблицы значениями из словаря
    for key, val in data.items():
        a = val + [key]
        tab3.add_row(a)
    print(tab3)

    # Возврат в меню
    input('Нажмите любую кнопку для продолжения. ')


def find_phone_number():
    """Функция поиска номера телефона по фамилии"""

    data = read()

    while True:

        find_key = input_surname(data)

        print(f'Номер телефона учащегося {data[find_key][0]} - {find_key}')

        print('Хотите продолжить поиск?(да/нет)')
        answer = input()

        if answer == 'нет':
            break
        elif answer == 'да':
            print('Породолжение...')
        else:
            print('Что- то пошло не так =(')
            print('Ответ неодназначен. Возврат в меню.')
            break
