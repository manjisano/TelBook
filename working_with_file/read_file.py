def read():
    """Функция считывающая данные из файлы и преобразующая их в словарь
    Выходные данные:
        database - база данных """

    file_name = 'C:/Users/winre/PycharmProjects/TelBook/data.txt'

    with open(file_name, 'r') as f:
        ar = f.readlines()

    # Разбиение строк на массивы
    new_ar = []
    for i in range(len(ar)):
        a = ar[i].split()
        new_ar.append([el.rstrip() for el in a])

    # Составление словаря из полученных массивов
    database = {}
    for i in range(len(new_ar)):
        database[new_ar[i][0]] = new_ar[i][1:]

    return database
