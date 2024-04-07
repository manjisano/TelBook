from prettytable import PrettyTable


def menu() -> int:
    """Функция вывода меню
    Выходные данные:
    num - номер пункта меню"""

    # Вывод меню
    print(' МЕНЮ '.center(40, "─"))
    print('1. Просмотр всех записей в базе данных')
    print('2. Добавление записей')
    print('3. Удаление записи по ключу')
    print('4. Изменение записи')
    print('5. Поиск необходимой информации')
    print('6. Завершение работы с базой данных\n')

    # Ввод значения и проверка корректности введенного значения
    while True:
        try:
            menu_item = int(input('Выберите пункт меню для продолжения: '))

            if (menu_item < 1) or (menu_item > 6):
                print('Что-то пошло не так =(')
                print('Некорректно введен пункт меню (значение не попадает в диапозон от 1 до 6). Попробуйте снова.')
            else:
                break

        except ValueError:
            print('Что-то пошло не так =(')
            print('Неверно введен пункт меню (необходимо ввести одно целое число). Попробуйте снова')

    return menu_item


def check_data(data: dict):
    """Функция вывода базы данных
    Входные данные:
    data - база данных"""

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

    tab3.field_names = ['Фамилия', 'Имя', 'Телефон']
    tab3.align['Фамилия'] = 'l'
    tab3.align['Имя'] = 'с'
    tab3.align['Телефон'] = 'r'
    tab3.sortby = 'Фамилия'

    # Заполнение таблицы значениями из словаря
    for key, val in data.items():
        a = val + [key]
        tab3.add_row(a)
    print(tab3)

    answer = ''
    while answer != 'да':
        print('Вернуться в меню?(для возврата напишите "да")')
        answer = input()


def new_data(data: dict) -> dict:
    """Функция добавления новой записи в базу данных
    Входные данные:
    data - база данных
    Выходные данные:
    data - база данных"""

    while True:

        print('Хотите добавить запись?')
        answer = input().lower()

        if answer == 'да':
            while True:

                print('Введите фамилию и имя нового учащегося:')
                surname, name = input().split()
                # Проверка на ввод букв
                if not (surname.isalpha() and name.isalpha()):
                    print('Что- то пошло не так =(')
                    print('Скорее всего вместо букв были использованы цифры.')
                    continue

                print('Введите номер телефона: ')
                phone_number = input()
                # Проверка на ввод цифр
                if not phone_number.isdigit():
                    print('Что- то пошло не так =(')
                    print('Скорее всего вместо цифр были использованы буквы.')
                    continue
                # Проверка на кол-во цифр в номере
                if len(phone_number) == 11:
                    break
                print('Неправильно веден номер. Кол-во цифр больше или меньше нужного.')

            data[phone_number] = [surname, name]
            print('Ученик успешно добавлен')

            answer = input('Для того, чтобы продолжить нажмите любую клавишу. Для выхода нажмите "1" ').lower()
            if answer == '1':
                break

        elif answer == 'нет':
            break

        else:
            print('Что- то пошло не так =(')
            print('Скорее всего ответ на вопрос неккоректен ответьте однозначно(да/нет)')
            continue

        return data


def delete_data(data: dict) -> dict:
    """Функция удаления элемента из базы данных
    Входные данные:
    data - база данных
    Выходные данные:
    data - база данных"""

    while True:
        print('Хотите удалить запись?')
        answer = input().lower()
        if answer == 'да':

            print('Введите фамилию учащегося, которого хотите удалить из базы: ')
            surname = input().capitalize()
            if not surname.isalpha():
                print('Что- то пошло не так =(')
                print('Скорее всего вместо букв были использованы цифры.')
                break
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

            flag = True
            for key, val in data.items():
                if k < 2:
                    if val[0] == surname:
                        del_key = key
                        flag = False
                        break
                else:
                    if val[0] == surname and val[1] == name:
                        del_key = key
                        flag = False
                        break

            if flag:
                print('Такого учащегося нет')
            else:
                del data[del_key]
                print('Учащийся успешно удален')
                continue

        elif answer == 'нет':
            break

        else:
            print('Что- то пошло не так =(')
            print('Скорее всего ответ на вопрос неккоректен ответьте однозначно(да/нет)')
            continue
    return data


def change_data(data: dict) -> dict:
    """Функция изменения элемента в базе данных
    Входные данные:
    data - база данных
    Выходные данные:
    new_data - база данных
    data - база данных"""
    while True:
        print('Хотите изменить запись?')
        answer = input().lower()

        if answer == 'да':
            print('Введите фамилию ')


def find_phone_number(data: dict):
    """Функция поиска номера телефона по фамилии
    Входные данные:
    data - база данных"""
    while True:
        print('Хотите удалить запись?')
        answer = input().lower()
        if answer == 'да':
            print('Введите фамилию учащегося, чей номер необходимо найти: ')
            surname = input().capitalize()
            if not surname.isalpha():
                print('Что- то пошло не так =(')
                print('Скорее всего вместо букв были использованы цифры.')
                break
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

        elif answer == 'нет':
            break

        else:
            print('Что-то пошло не так =(')
            print('Скорее всего ответ на вопрос неккоректен ответьте однозначно(да/нет)')
            continue


data = {'89105632512': ['Шарапов', 'Василий'],
        '89156214578': ['Кузьмин', 'Иннокентий'],
        '89201235896': ['Добрынин', 'Фёдор'],
        '89523215613': ['Сорокин', 'Егор'],
        '89156321547': ['Мартышкин', 'Макар'],
        '89109029755': ['Рожкин', 'Роман'],
        '89105632532': ['Маврина', 'Марина'],
        '89206548912': ['Дубинина', 'Евгения'],
        '89802364565': ['Сорокин', 'Назар']}

while True:
    num = menu()
    match num:
        case 1:
            check_data(data)
        case 2:
            data = new_data(data)
        case 3:
            data = delete_data(data)
        case 4:
            data = change_data(data)
        case 5:
            find_phone_number(data)
        case 6:
            print('Программа завершает работу')
            break
