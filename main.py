from working_with_database import *


def menu() -> int:
    """Функция вывода меню
    Выходные данные:
    menu_item - номер пункта меню"""

    # Вывод меню
    print(' МЕНЮ '.center(40, "─"))
    print('1. Просмотр всех записей в базе данных')
    print('2. Добавление записей')
    print('3. Удаление записи')
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


while True:
    num = menu()
    match num:
        case 1:
            viewing_data.check_data()
        case 2:
            changes_in_data.new_data()
        case 3:
            changes_in_data.delete_data()
        case 4:
            changes_in_data.change_data()
        case 5:
            viewing_data.find_phone_number()
        case 6:
            print('Программа завершает работу')
            break
