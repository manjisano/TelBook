def input_surname(data):

    while True:
        print('Введите фамилию учащегося: ')
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
        else:
            break

    return find_key