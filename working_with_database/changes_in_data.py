from working_with_file import *


def new_data():
    """Функция добавления новой записи в базу данных"""

    data = read_file.read()

    while True:
        print('Введите ФИО нового учащегося:')
        surname, name, second_name = input().split()

        # Проверка на ввод букв
        if not (surname.isalpha() and name.isalpha() and second_name.isalpha()):
            print('Что-то пошло не так =(')
            print('Скорее всего вместо букв были использованы цифры.')
            continue

        print('Введите номер телефона: ')
        phone_number = input()

        # Проверка на ввод цифр
        if not phone_number.isdigit():
            print('Что-то пошло не так =(')
            print('Скорее всего вместо цифр были использованы буквы.')
            continue

        # Проверка на кол-во цифр в номере
        if len(phone_number) != 11:
            print('Неправильно веден номер. Кол-во цифр больше или меньше нужного.')
            continue

        data[phone_number] = [surname.capitalize(), name.capitalize(), second_name.capitalize()]
        changes_in_file.overwrite(data)
        print('Ученик успешно добавлен')
        break



def delete_data():
    """Функция удаления элемента из базы данных"""

    data = read_file.read()

    while True:

        print('Введите фамилию учащегося, которого хотите удалить из базы: ')
        surname = input().capitalize()

        # Проверка на ввод букв
        if not surname.isalpha():
            print('Что-то пошло не так =(')
            print('Скорее всего вместо букв были использованы цифры.')
            continue

        # Проверка на кол-во учащихся с одинаковой фамилией
        k = 0
        for val in data.values():
            if val[0] == surname:
                k += 1

        if k >= 2:
            print('Учащихся с такой фамилие несколько. Уточните Имя')
            name = input().capitalize()
            if not name.isalpha():
                print('Что-то пошло не так =(')
                print('Скорее всего вместо букв были использованы цифры.')
                continue

        # Поиск ключа по значению
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

        # Удаление учащегося по ключу
        if flag:
            print('Такого учащегося нет')
        else:
            del data[del_key]
            changes_in_file.overwrite(data)
            print('Учащийся успешно удален')
            break



def change_data():
    """Функция изменения элемента в базе данных"""

    data = read_file.read()

    while True:

        print('Введите фамилию: ')
        surname = input().capitalize()

        # Проверка на ввод букв
        if not surname.isalpha():
            print('Что- то пошло не так =(')
            print('Скорее всего вместо букв были использованы цифры.')
            continue

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
                continue

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
            continue

        # Вывод меню
        print(f'Учащийся(аяся) {data[find_key][0] + " " +  data[find_key][1] + " " + data[find_key][2]}, телефон - {find_key}')
        print(f'Что хотите изменить: ')
        print('1. Фамилию')
        print('2. Имя')
        print('3. Отчество')
        print('4. Телефон')

        # Ввод и проверка на правильность ввода
        try:
            menu_item = int(input('Выберите пункт меню для продолжения: '))

            if (menu_item < 1) or (menu_item > 4):
                print('Что-то пошло не так =(')
                print('Некорректно введен пункт меню (значение не попадает в диапозон от 1 до 4). Попробуйте снова.')
                continue

        except ValueError:
            print('Что-то пошло не так =(')
            print('Неверно введен пункт меню (необходимо ввести одно целое число). Попробуйте снова')
            continue

        match menu_item:
            case 1:
                # Изменение фамилии
                print('Введите новую фамилию:')
                surname = input().capitalize()

                if not surname.isalpha():
                    print('Что- то пошло не так =(')
                    print('Скорее всего вместо букв были использованы цифры.')
                    continue
                data[find_key][0] = surname

            case 2:
                # Изменение имени
                print('Введите новое имя:')
                name = input().capitalize()

                if not surname.isalpha():
                    print('Что- то пошло не так =(')
                    print('Скорее всего вместо букв были использованы цифры.')
                    continue
                data[find_key][1] = name

            case 3:
                # Изменение отчества
                print('Введите новое отчество:')
                second_name = input().capitalize()

                if not surname.isalpha():
                    print('Что- то пошло не так =(')
                    print('Скорее всего вместо букв были использованы цифры.')
                    continue
                data[find_key][2] = second_name

            case 4:
                # Изменение номера телефона
                print('Введите номер телефона: ')
                phone_number = input()

                # Проверка на ввод цифр
                if not phone_number.isdigit():
                    print('Что-то пошло не так =(')
                    print('Скорее всего вместо цифр были использованы буквы.')
                    continue

                # Проверка на кол-во цифр в номере
                if len(phone_number) != 11:
                    print('Неправильно веден номер. Кол-во цифр больше или меньше нужного.')
                    continue
                data[phone_number] = data.pop(find_key)

        changes_in_file.overwrite(data)
        break


