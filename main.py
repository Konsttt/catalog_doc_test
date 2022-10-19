# Task5_function

# Задание 1
# p - people команда, которая спросит номер документа и выведет имя человека, которому он принадлежит
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится
#     Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин"
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его
# номер, тип, имя владельца и номер полки, на котором он будет храниться.
# Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def get_name(doc_catalog):
    '''Print name from documents

    The program requests the document number and return person name.
    Arguments: your catalog with documents - it's list with dict'''

    number_ = input('Введите номер документа: ')
    name_ = 'Документ с таким номером не существует.'
    for doc in doc_catalog:
        if doc['number'] == number_:
            name_ = doc['name']
            break
    print(name_)
    return name_


def get_shelf(shelf_catalog):
    '''Print shelf number from shelf catalog

    The program requests the document number and return shelf number.
    Arguments: your catalog with shelf - it's a dict; dict values - lists.'''

    number_ = input('Введите номер документа: ')
    shelf_number = 'Документа с таким номером не существует.'
    for k, v in shelf_catalog.items():
        if number_ in v:
            shelf_number = k
            break
    print(shelf_number)
    return shelf_number


def get_all_doc(doc_catalog):
    '''Print type, number and name all person from doc catalog

    Arguments: your catalog with documents - it's list with dict'''
    view_list = []
    for doc in doc_catalog:
        view_list.append(f'{doc["type"]} "{doc["number"]}" "{doc["name"]}"')
    for _ in view_list:
        print(_)
    return view_list


def add_person(doc_catalog, shelf_catalog):
    '''Add new person in doc catalog and add doc catalog to shelf.

    Arguments: doc_catalog - list wiht dict; shelf_catalog - dict with list value.
    The program requests the document number, type, person name and shelf number
    Also by entering Q you can find out the numbers of all shelves'''

    print('Добавление нового документа в каталог и размещение документа на полке.')

    number_ = None
    flag1 = True  # для зацикливания ввода номера документа, пока не будет введён уникальный
    while flag1:
        number_ = input('Введите номер документа: ')
        flag2 = False  # для обработки Y/N
        for item in doc_catalog:
            if item['number'] == number_:
                print('Документ с таким номером уже существует')
                confirm_ = input('Выйти из программы? Y/N')
                if confirm_ == 'Y':
                    print('Программа добавления нового документа завершена.')
                    return
                else:
                    flag2 = True  # Вводим номер ещё раз
        if flag2:
            flag1 = True
        else:
            flag1 = False

    type_ = input('Введите тип документа: ')
    name_ = input('Введите имя владельца: ')

    doc_catalog.append({'number': number_, 'type': type_, 'name': name_})
    flag = True

    shelf_list_ = [k for k in shelf_catalog]

    shelf_ = 1
    while flag:
        shelf_ = input('Введите номер полки для документа: ')
        if shelf_ in shelf_list_:
            flag = False
        else:
            print('Полки с таким номером не существует. Попробуйте ещё раз.')
            q_ = input('Чтобы узнать существующие номера полок введите символ Q: ')
            if q_ == 'Q':
                print(shelf_list_)
    shelf_doc_list = shelf_catalog[shelf_]
    shelf_doc_list.append(number_)
    shelf_catalog[shelf_] = shelf_doc_list
    print()
    s = f'Документ - {type_} с номером {number_} владельца {name_} успешно размещен на полке {shelf_}'
    print(s)
    return s


# def get_all_shelf(shelf_catalog):
#     '''Return all shelf number from catalog.
#
#     Arguments: dict with keys - shelf number (saved like string) and values - list with doc numbers.'''
#     shelf_list = []
#     for shelf in shelf_catalog:
#         shelf_list.append(shelf)
#     return shelf_list


# get_name(documents)
# get_shelf(directories)
# get_all_doc(documents)
# add_person(documents, directories)
# print('_'*100)
# get_all_doc(documents)


# Задача №2
def del_doc(doc_catalog, shelf_catalog):
    '''Delete document from doc catalog and from shelf.

    Arguments: doc_catalog - list with dict; shelf_catalog - dict with list value.
    The program requests the document number, which will be deleted.'''
    flag = True
    del_item = None
    number_ = None

    while flag:
        number_ = input('Введите номер документа, который хотите удалить из каталога: ')
        for doc in doc_catalog:
            if number_ == doc['number']:
                del_item = doc
                flag = False
                break
        else:
            exit_ = input('Такого номера не существует. Выйти из программы? Y/N')
            if exit_ == 'Y':
                print('Завершение работы программы del_doc.')
                return

    #  Блок подтверждения удаления и удаление записи по значению.
    confirm = input(f'Вы действительно хотите удалить документ {number_} ? Y/N : ')
    if confirm == 'Y':
        doc_catalog.remove(del_item)
        for k, v in shelf_catalog.items():
            if number_ in v:
                v.remove(number_)
                s = f'Документ {number_} успешно удалён из каталога и с полки {k}.'
                print(s)
                return s
    else:
        print('Отмена удаления. Завершение работы программы del_doc.')
        return 'Отмена удаления. Завершение работы программы del_doc.'


# add_person(documents, directories)
# get_all_doc(documents)
# del_doc(documents, directories)
# get_all_doc(documents)


# Функция проверки существования документа
def check_doc(doc_catalog, number):
    for doc in doc_catalog:
        if number == doc['number']:
            return True
    return False


# Функция проверки существования полки
def check_shelf(shelf_catalog, shelf_number):
    for shelf in shelf_catalog:
        if shelf_number == shelf:
            return True
    return False


# Функция проверки, что документ уже лежит на этой полке
def same_shelf(shelf_catalog, shelf_number, doc_number):
    for k, v in shelf_catalog.items():
        if doc_number in v and k == shelf_number:
            return True
    return False


# Функция по номеру документа возвращает номер полки
def get_shelf_old(shelf_catalog, number_):
    shelf_number = None
    for k, v in shelf_catalog.items():
        if number_ in v:
            shelf_number = k
            break
    return shelf_number


# Функция перемещения документа с полки на полку.

def move_doc(doc_catalog, shelf_catalog):
    number_ = None
    shelf_number_ = None

    flag = True
    while flag:
        number_ = input('Введите номер документа, который хотите переместить на новую полку: ')
        if check_doc(doc_catalog, number_):
            flag = False
        else:
            confirm = input(f'Документа с номером {number_} не существует. Выйти из программы? Y/N')
            if confirm == 'Y':
                print('Завершение работы программы mov_doc.')
                return

    flag = True
    while flag:
        shelf_number_ = input(f'Введите номер полки, на которую переместить документ с номером {number_}: ')
        if check_shelf(shelf_catalog, shelf_number_):
            if same_shelf(shelf_catalog, shelf_number_, number_):
                confirm = input(
                    f'Документ с номером {number_} уже находится на полке {shelf_number_}. Выйти из программы? Y/N')
                if confirm == 'Y':
                    print('Завершение работы программы mov_doc.')
                    return
                else:
                    flag = True
            else:
                flag = False
        else:
            confirm = input(f'Полки с номером {shelf_number_} не существует. Выйти из программы? Y/N')
            if confirm == 'Y':
                print('Завершение работы программы mov_doc.')
                return
            else:
                flag = True

    old_shelf = get_shelf_old(shelf_catalog, number_)
    # добавление на новую полку
    # shelf_doc_list = shelf_catalog[shelf_number_]
    # shelf_doc_list.append(number_)
    # shelf_catalog[shelf_number_] = shelf_doc_list
    shelf_catalog[shelf_number_].append(number_)

    # удаление со старой полки
    # shelf_doc_list = shelf_catalog[old_shelf]
    # shelf_doc_list.remove(number_)
    # shelf_catalog[old_shelf] = shelf_doc_list
    shelf_catalog[old_shelf].remove(number_)
    s = f'Документ с номером {number_} успешно перемещён с полки {old_shelf} на полку {shelf_number_}'
    print(s)
    return s


# Добавление новой полки
def add_shelf(shelf_catalog):
    flag = True
    new_shelf_ = 'default'

    while flag:
        new_shelf_ = input(f'Введите номер новой полки, которую хотите добавить')
        for shelf in shelf_catalog:
            if new_shelf_ == shelf:
                confirm = input(f'Полка с номером {new_shelf_} уже существует. Выйти из программы? Y/N')
                if confirm == 'Y':
                    print('Завершение работы программы add_shelf.')
                    return
                else:
                    flag = True
                    break
            else:
                flag = False

    shelf_catalog[new_shelf_] = []
    s = f'Новая полка номер {new_shelf_} успешно добавлена в каталог.'
    print(s)
    return s


# add_person(documents, directories)
# print('____________________________________')
# get_all_doc(documents)
# print(directories)
# print('____________________________________')
# move_doc(documents, directories)
# print('____________________________________')
# print(directories)
#
# add_shelf(directories)
# print('____________________________________')
# print(directories)

# Пользовательский ввод команд
def catalog_prog(doc_catalog, shelf_catalog):
    print("Программа работы с каталогом.")
    print("Команды:\n\
        'p' - вывести имя человека по номеру документа\n\
        's - вывести номер полки документа по номеру документа'\n\
        'l' - вывод списка всех документов\n\
        'a' - добавление документа в каталог\n\
        'd' - удаление документа по номеру из каталога\n\
        'm' - перемещение документа с полки на полку\n\
        'as' - добавление новой полки\n\
        'q' - выход из программы")

    flag = True
    while flag:
        command_ = input('Введите команду: ')
        if command_ == 'p':
            get_name(doc_catalog)
        elif command_ == 's':
            get_shelf(shelf_catalog)
        elif command_ == 'l':
            get_all_doc(doc_catalog)
        elif command_ == 'a':
            add_person(doc_catalog, shelf_catalog)
        elif command_ == 'd':
            del_doc(doc_catalog, shelf_catalog)
        elif command_ == 'm':
            move_doc(doc_catalog, shelf_catalog)
        elif command_ == 'as':
            add_shelf(shelf_catalog)
        elif command_ == 'q':
            flag = False
            print('Завершение работы. Выполнен выход из программы.')
        print()
    return True


if __name__ == '__main__':
    catalog_prog(documents, directories)
