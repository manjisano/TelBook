def overwrite(database):
    """Функция перезаписи данных в файле
    Входные данные:
        database - база данных"""

    file_name = 'C:/Users/winre/PycharmProjects/KursachCeH9/data.txt'

    with open(file_name, 'w') as f:
        for key, val in database.items():
            s = key + '\t' + '\t'.join(val) + '\n'
            f.write(s)
