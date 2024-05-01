from prettytable import PrettyTable


def menu():
    # Функция вывода меню
    # Выходные данные:
    # num - номер пункта меню

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
    # Функция вывода базы данных
    # Входные данные:
    # data - база данных

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
        a = [key] + val
        tab3.add_row(a)
    print(tab3)


def new(data):
    # Функция добавления новой записи в базу данных
    # Входные данные:
    # data - база данных
    # Выходные данные:
    # data - база данных

    while True:

        print('Добавить запись?')
        answer = input().lower()

        if answer == 'да':
            print('Введите ФИ нового учащегося:')
            surname, name = input().split()

            # Проверка на ввод букв
            if not (surname.isalpha() and name.isalpha()):
                print('Скорее всего вместо букв были использованы цифры.')
                continue

            print('Введите пол нового учащегося: ')
            gender = input().lower()

            # Проверка на правильность ввода
            if gender != 'мужской' and gender != 'женский':
                print('Пол введен неверно')
                continue

            print('Введите вес и рост: ')
            weight, height = input().split()

            #Проверка на ввод чисел
            if not(weight.isdigit() and height.isdigit()):
                continue

            data[surname] = [name.capitalize(), gender, weight, height]
            print('Ученик успешно добавлен')

        elif answer == 'нет':
            break

        else:
            print('Скорее всего ответ на вопрос неккоректен ответьте однозначно(да/нет)')
            continue

    return data


def delete(data):
    # Функция удаления элемента из базы данных
    # Входные данные:
    # data - база данных
    # Выходные данные:
    # data - база данных

    while True:
        print('Удалить запись?')
        answer = input().lower()

        if answer == 'да':

            print('Введите фамилию учащегося, которого хотите удалить из базы: ')
            surname = input().capitalize()

            # Проверка на ввод букв
            if not surname.isalpha():
                print('Фамилия должна состоять из букв.')
                break

            # Удаление учащегося по ключу
            if surname in data:
                del data[surname]
                print('Учащийся успешно удален')
                continue
            else:
                print('Такого учащегося нет')

        elif answer == 'нет':
            break

        else:
            print('Скорее всего ответ на вопрос неккоректен ответьте однозначно(да/нет)')
            continue

    return data


def change(data):
    #Функция изменения элемента в базе данных
    #Входные данные:
    #data - база данных
    #Выходные данные:
    #data - база данных

    while True:
        print('Изменить запись?')
        answer = input().lower()

        if answer == 'да':
            print('Введите фамилию ')
            surname = input().capitalize()

            # Проверка на ввод букв
            if not surname.isalpha():
                print('Скорее всего вместо букв были использованы цифры.')
                continue

            # Проверка на наличие в базе данных
            if not(surname in data):
                print('Такого учащегося нет')
                continue

            # Вывод меню
            print(f'Учащийся(аяся) {surname}')
            print(f'Что хотите изменить: ')
            print('1. Фамилию')
            print('2. Имя')
            print('3. Пол')
            print('4. Вес')
            print('5. Рост')

            # Ввод и проверка на правильность ввода
            m = int(input('Выберите пункт меню для продолжения: '))

            if (m < 1) or (m > 5):
                print('Некорректно введен пункт меню.')
                continue

            match m:
                case 1:
                    # Изменение фамилии
                    print('Введите новую фамилию:')
                    surname = input().capitalize()

                    # Проверка на ввод букв
                    if not surname.isalpha():
                        print('Скорее всего вместо букв были использованы цифры.')
                        continue

                    data[surname] = data.pop(surname)

                case 2:
                    # Изменение имени
                    print('Введите новое имя:')
                    name = input().capitalize()

                    # Проверка на ввод букв
                    if not surname.isalpha():
                        print('Что- то пошло не так =(')
                        print('Скорее всего вместо букв были использованы цифры.')
                        continue

                    data[surname][0] = name

                case 3:
                    # Изменение пола
                    print('Введите новый пол:')
                    gender = input().lower()

                    # Проверка на правильность ввода
                    if gender != 'мужской' or gender != 'женский':
                        print('Пол введен неверно')
                        continue

                    data[surname][1] = gender

                case 4:
                    # Изменение веса
                    print('Введите вес: ')
                    weight = input()

                    # Проверка на ввод чисел
                    if not (weight.isdigit()):
                        print('Неверный ввод')
                        continue

                    data[surname][2] = weight

                case 5:
                    # Изменение роста
                    print('Введите рост: ')
                    height = input()

                    # Проверка на ввод чисел
                    if not (height.isdigit()):
                        print('Неверный ввод')
                        continue

                    data[surname][3] = height

        elif answer == 'нет':
            break

        else:
            print('Что-то пошло не так =(')
            print('Скорее всего ответ на вопрос неккоректен ответьте однозначно(да/нет)')
            continue

    return data


def find(data):
    #Функция поиска ср. веса мальчиков, ср.роста девочек, и самого высокого учащегося
    #Входные данные:
    #data - база данных

    # Поиск суммы всей массы мальчиков и суммы всех ростов девочек, а также их кол-ва
    sum_male = c_male = sum_female = c_female = 0
    for key in data:
        if data[key][1] == 'мужской':
            sum_male += float(data[key][2])
            c_male += 1
        else:
            sum_female += float(data[key][3])
            c_female += 1

    print(f'Средний вес мальчиков - {sum_male/c_male}, средний рост девочек - {sum_female/c_female}')

    maxh = 0
    for key in data:
        if float(data[key][3]) > maxh:
            maxh_key = key
            maxh = float(data[key][3])

    print(f'Самый высокий(ая) {maxh_key}, его(её) рост - {data[maxh_key][3]}')


data = {'Савушкин': ['Василий', 'мужской', '64.3', '172'],
        'Королёв': ['Николай', 'мужской', '57.7', '168'],
        'Гуськова': ['Алина', 'женский', '57', '167'],
        'Герасин': ['Илья', 'мужской', '73', '170'],
        'Дукмасова': ['Аполлинария', 'женский', '54', '166'],
        'Водяницкая': ['Нелли', 'женский', '56', '164'],
        'Быковский': ['Леонид', 'мужской', '51', '171'],
        'Кузнецова': ['Ксения', 'женский', '63', '178'],
        'Кравцов': ['Иван', 'мужской', '72', '174'],
        'Егорова': ['Елена', 'женский', '49', '161']}

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
            print('Завершение работы')
            break
