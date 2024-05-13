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











data = {'89105632512': ['Шарапов', 'Василий', 'Олегович'],
        '89156214578': ['Кузьмин', 'Иннокентий', 'Алексеевич'],
        '89201235896': ['Добрынин', 'Фёдор', 'Сергеевич'],
        '89523215613': ['Сорокин', 'Егор', 'Ильич'],
        '89156321547': ['Мартышкин', 'Макар', 'Александрович'],
        '89109029755': ['Рожкин', 'Роман', 'Сергеевич'],
        '89105632532': ['Маврина', 'Марина', 'Антоновна'],
        '89206548912': ['Дубинина', 'Евгения', 'Евгеньевич'],
        '89802364565': ['Сорокин', 'Назар', 'Степанович']}

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
