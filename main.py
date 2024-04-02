def menu() -> int:
    """Функция вывода меню
    Выходные данные:
    num - номер пункта меню"""

    #Вывод меню
    print(' МЕНЮ: '.center(40, "-"))
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
                print('Некорректно введен пункт меню (значение не попадает в диапозон от 1 до 6. Попробуйте снова.')
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

    print('Фамилия'.center(15), 'Имя'.center(12),
          'Телефон'.center(17),
          'Дата рождения'.center(15))

    print(''.center(15, '-'), ''.center(12, '-'),
          ''.center(17, '-'), ''.center(15, '-'))

    for key, val in data.items():

        print('{0:<15s}'.format(val[0]),
              '{0:<12s}'.format(val[1]),
              key.center(17), val[2].center(12))

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

        answer = ''
        print('Хотите добавить запись?')
        answer = input().lower()

        if answer == 'да':

            print('Введите Имя Фамилию нового учащегося:')
            surname, name = input().split()

            print(f'Введите номер телефона {surname.title()} {name.title()}: ')
            phone_number = ''

            while True:
                phone_number = input()
                if len(phone_number) == 11:
                    break
                print('Неправильно веден номер. Кол-во цифр больше или меньше нужного.')

            data[phone_number] = [surname, name]
            print('Ученик успешно добавлен')

            answer = input('Для того, чтобы продолжать нажмите любую клавишу. Для выхода нажмите "q" ').lower()
            if answer == 'q':
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


def change_data(data: dict) -> dict:
    """Функция изменения элемента в базе данных
    Входные данные:
    data - база данных
    Выходные данные:
    data - база данных"""


def find_phone_number(data: dict):
    """Функция поиска номера телефона по фамилии
    Входные данные:
    data - база данных
    Выходные данные:
    data - база данных"""


data = {'89105632512': ['Шарапов', 'Василий',
                        '10.12.2001'],
        '89156214578': ['Кузьмин', 'Иннокентий',
                        '12.05.1998'],
        '89201235896': ['Добрынин', 'Фёдор',
                        '13.01.2000'],
        '89523215613': ['Сорокин', 'Егор',
                        '25.05.1998'],
        '89156321547': ['Мартышкин', 'Макар',
                        '16.06.1996'],
        '89109029755': ['Рожкин', 'Роман',
                        '31.12.2002'],
        '89105632532': ['Маврина', 'Марина',
                        '08.03.2003'],
        '89206548912': ['Дубинина', 'Евгения',
                        '17.08.2000'],
        '89802364565': ['Сорокин', 'Назар',
                        '15.07.1995']}


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
