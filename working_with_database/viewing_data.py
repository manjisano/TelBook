from prettytable import PrettyTable

from working_with_file.read_file import read


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

    tab3.field_names = ['Фамилия', 'Имя', 'Отчество','Телефон']
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
    answer = ''
    while answer != 'y':
        print('Вернуться в меню?(для возврата напишите "y")')
        answer = input()


def find_phone_number():
    """Функция поиска номера телефона по фамилии"""

    data = read()

    while True:

        print('Хотите найти запись?')
        answer = input().lower()

        if answer == 'y':

            print('Введите фамилию учащегося, чей номер необходимо найти: ')
            surname = input().capitalize()

            if not surname.isalpha():
                print('Что- то пошло не так =(')
                print('Скорее всего вместо букв были использованы цифры.')
                break

            # Проверка на кол-во учащихся с одинаковой фамилией
            k = 0
            for val in data.values():
                if val[0] == surname:
                    k += 1

            if k >= 2:
                print('Учащихся с такой фамилие несколько. Уточните Имя')
                name = input().capitalize()
                if not name.isalpha():
                    print('Что- то пошло не так =(')
                    print('Скорее всего вместо букв были использованы цифры.')
                    break

            # Поиск ключа по значению
            flag = True
            for key, val in data.items():
                if k < 2:
                    if val[0] == surname:
                        find_key = key
                        flag = False
                        break
                else:
                    if val[0] == surname and val[1] == name:
                        find_key = key
                        flag = False
                        break

            if flag:
                print('Такого учащегося нет')
            else:
                print(f'Номер телефона учащегося {surname} - {find_key}')
                continue

        elif answer == 'n':
            break

        else:
            print('Что-то пошло не так =(')
            print('Скорее всего ответ на вопрос неккоректен ответьте однозначно(y/n)')
            continue
