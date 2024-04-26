from prettytable import PrettyTable


def menu():
    #Функция вывода меню
    #Выходные данные:
    #num - номер пункта меню

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
        num = int(input('Выберите пункт меню: '))

        if (num < 1) or (num > 6):
            print('Неправильный пункт меню.')
        else:
            break

    return num


def watch(data):
    #Функция вывода базы данных
    #Входные данные:
    #data - база данных

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

    tab3.field_names = ['Фамилия', 'Имя', 'Пол', 'Вес', 'Рост']
    tab3.align['Фамилия'] = 'l'
    tab3.align['Имя'] = 'с'
    tab3.align['Пол'] = 'с'
    tab3.align['Вес'] = 'c'
    tab3.align['Рост'] = 'r'
    tab3.sortby = 'Фамилия'

    # Заполнение таблицы значениями из словаря
    for key, val in data.items():
        a = val + [key]
        tab3.add_row(a)
    print(tab3)


data = {}

while True:
    n = menu()
    match n:
        case 1:
            watch(data)
        case 2:
            data = new(data)
        case 3:
            data = delete(data)
        case 4:
            data = change(data)
        case 5:
            find(data)
        case 6:
            print('Программа завершает работу')
            break