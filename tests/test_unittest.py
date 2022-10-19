import unittest
from unittest.mock import patch
from parameterized import parameterized  # Библиотека в дополнение к unittest
from main import get_name, get_shelf, get_all_doc, add_person, del_doc, documents, directories, check_doc, \
    check_shelf, same_shelf, get_shelf_old, move_doc, add_shelf, catalog_prog


documents_del = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories_del = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

documents_move = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories_move = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

directories_add_shelf = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

FIXTURES_NUMBERS_NAMES = [('2207 876234', 'Василий Гупкин'),
                          ('11-2', 'Геннадий Покемонов'),
                          ('10006', 'Аристарх Павлов'),
                          ('000', 'Документ с таким номером не существует.'),
                          (None, 'Документ с таким номером не существует.')
                          ]

FIXTURES_NUMBERS_SHELVES = [('2207 876234', '1'),
                            ('11-2', '1'),
                            ('10006', '2'),
                            ('5455 028765', '1'),
                            ('000', 'Документа с таким номером не существует.'),
                            ('', 'Документа с таким номером не существует.'),
                            (None, 'Документа с таким номером не существует.')
                            ]

FIXTURES_DOCUMENTS = [([{"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
                        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
                        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}],
                       ['passport "2207 876234" "Василий Гупкин"', 'invoice "11-2" "Геннадий Покемонов"',
                        'insurance "10006" "Аристарх Павлов"']),
                      ([{"type": "passport", "number": "11111", "name": "Василий Васин"},
                        {"type": "passport", "number": "33333", "name": "Иван Иванов"}],
                       ['passport "11111" "Василий Васин"', 'passport "33333" "Иван Иванов"'])
                      ]

FIXTURES_ADD_DOCUMENTS = [('007', 'passport', 'James Bond', '3',
                           'Документ - passport с номером 007 владельца James Bond успешно размещен на полке 3'),
                          ('001', 'passport', 'Петр Петров', '1',
                           'Документ - passport с номером 001 владельца Петр Петров успешно размещен на полке 1')
                          ]

FIXTURES_DEL_DOC = [('11-2', 'Y', 'Документ 11-2 успешно удалён из каталога и с полки 1.'),
                    ('10006', 'N', 'Отмена удаления. Завершение работы программы del_doc.')
                    ]

FIXTURES_CHECK_DOC = [('11-2', True), ('000', False), ('10006', True)]

FIXTURES_CHECK_SHELF = [('1', True), ('5', False), ('3', True)]

FIXTURES_SAME_SHELF = [('1', '11-2', True), ('2', '10006', True), ('1', '2207 876234', True), ('3', '111', False)]

FIXTURES_GET_SHELF_OLD = [('11-2', '1'), ('10006', '2'), ('2207 876234', '1'), ('111', None)]

FIXTURES_MOVE_DOC = [('11-2', '3', 'Документ с номером 11-2 успешно перемещён с полки 1 на полку 3'),
                     ('10006', '1', 'Документ с номером 10006 успешно перемещён с полки 2 на полку 1'),
                     ('2207 876234', '3', 'Документ с номером 2207 876234 успешно перемещён с полки 1 на полку 3')]

FIXTURES_ADD_SHELF = [('5', 'Новая полка номер 5 успешно добавлена в каталог.'),
                      ('7', 'Новая полка номер 7 успешно добавлена в каталог.'),
                      ('9', 'Новая полка номер 9 успешно добавлена в каталог.')]


class TestCatalog(unittest.TestCase):

    def tearDown(self) -> None:
        print(f'___________________________________________________')

    @parameterized.expand(FIXTURES_NUMBERS_NAMES)
    @patch('builtins.input')
    def test_get_name(self, first_from_fixtures, second_from_fixtures, mock_obj):
        mock_obj.return_value = first_from_fixtures
        result = get_name(documents)
        self.assertEqual(second_from_fixtures, result)

    @parameterized.expand(FIXTURES_NUMBERS_SHELVES)
    @patch('builtins.input')
    def test_get_shelf(self, first_from_fixtures, second_from_fixtures, mock_obj):
        mock_obj.return_value = first_from_fixtures
        result = get_shelf(directories)
        self.assertEqual(second_from_fixtures, result)

    @parameterized.expand(FIXTURES_DOCUMENTS)
    def test_get_all_doc(self, first_from_fixtures, second_from_fixtures):
        result = get_all_doc(first_from_fixtures)
        self.assertEqual(second_from_fixtures, result)

    @parameterized.expand(FIXTURES_ADD_DOCUMENTS)
    @patch('builtins.input')
    def test_add_person(self, a, b, c, d, exp_result, mock_obj):
        mock_obj.side_effect = [a, b, c, d]  # функция, динамически подставляет из списка в каждый следующий input()
        result = add_person(documents, directories)
        self.assertEqual(exp_result, result)

    @parameterized.expand(FIXTURES_DEL_DOC)
    @patch('builtins.input')
    def test_del_doc(self, a, b, exp_result, mock_obj):
        mock_obj.side_effect = [a, b]  # функция, динамически подставляет из списка в каждый следующий input()
        result = del_doc(documents_del, directories_del)
        self.assertEqual(exp_result, result)

    @parameterized.expand(FIXTURES_CHECK_DOC)
    def test_check_doc(self, num_doc, exp_result):
        result = check_doc(documents, num_doc)
        self.assertEqual(exp_result, result)

    @parameterized.expand(FIXTURES_CHECK_SHELF)
    def test_check_shelf(self, num_doc, exp_result):
        result = check_shelf(directories, num_doc)
        self.assertEqual(exp_result, result)

    @parameterized.expand(FIXTURES_SAME_SHELF)
    def test_same_shelf(self, shelf_num, doc_num, exp_result):
        result = same_shelf(directories, shelf_num, doc_num)
        self.assertEqual(exp_result, result)

    @parameterized.expand(FIXTURES_GET_SHELF_OLD)
    def test_get_shelf_old(self, doc_num, exp_result):
        result = get_shelf_old(directories, doc_num)
        self.assertEqual(exp_result, result)

    @parameterized.expand(FIXTURES_MOVE_DOC)
    @patch('builtins.input')
    def test_move_doc(self, doc_num, shelf_num, exp_result, mock_obj):
        mock_obj.side_effect = [doc_num, shelf_num]
        result = move_doc(documents_move, directories_move)
        self.assertEqual(exp_result, result)

    @parameterized.expand(FIXTURES_ADD_SHELF)
    @patch('builtins.input')
    def test_add_shelf(self, shelf_num, exp_result, mock_obj):
        mock_obj.return_value = shelf_num  # функция, динамически подставляет из списка в каждый следующий input()
        result = add_shelf(directories_add_shelf)
        self.assertEqual(exp_result, result)

    @patch('builtins.input', return_value='q')
    def test_catalog_prog(self, mock_obj):
        result = catalog_prog(documents, directories)
        self.assertEqual(True, result)




