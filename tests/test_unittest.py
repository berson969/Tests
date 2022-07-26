import unittest
from unittest.mock import patch, MagicMock
from admincase import people, shelf, all_list, add_new, delete_doc, move_doc, add_shelf, main
from parameterized import parameterized


class TestAdminCase(unittest.TestCase):
    """AdminCase function tests"""

    @classmethod
    def setUpClass(cls):
        """Set up for class"""
        print("setUpClass")
        print("==========")

    @classmethod
    def tearDownClass(cls):
        """Tear down for class"""
        print("==========")
        print("tearDownClass")

    @parameterized.expand(
        [("passport", "2207 876234", "Василий Гупкин"),
         ("invoice", "11-2", "Геннадий Покемонов"),
         ("insurance", "10006", "Аристарх Павлов"),
         ("insurance", "106", "Аристарх Петров")]
    )
    def test_all_list(self, type, number, name):
        result_list = all_list()
        self.assertIn([type, number, name], result_list)

    @parameterized.expand(
        [('2207 876234', "Василий Гупкин"),
         ("106", "Аристарх Петров"),
         ('222', None)]
    )
    def test_people(self, doc_number, doc_name):
        result_name = people(doc_number)
        self.assertEqual(doc_name, result_name)

    @parameterized.expand(
        [('2207 876234', '1'),
         ("106", None),
         ('222', None)]
    )
    def test_shelf(self, doc_number, shelf_number):
        result_shelf_number = shelf(doc_number)
        if result_shelf_number is None:
            self.assertIsNone(result_shelf_number)
        self.assertEqual(shelf_number, result_shelf_number)

    @parameterized.expand(
        [("passport", "4505 2345", "Василий Иванов", '1'),
         ("insurance", "10006", "Аристарх Павлов", '1')]
    )
    def test_add_new(self, type_new, number_new, name_new, shelf_new):
        result = add_new(type_new, number_new, name_new, shelf_new)
        if result is None:
            self.assertIsNone(result)
        else:
            self.assertIn(number_new, result)

    @parameterized.expand(
        [("11-2", "Геннадий Покемонов"),
         ('111', None)]
    )
    def test_delete_doc(self, doc_number, name):
        result = delete_doc(doc_number)
        if result is None:
            self.assertIsNone(result)
        else:
            self.assertEqual(name, result)

    @parameterized.expand(
        [("11-2", '2'),
         ("106", '3'),
         ('11', '1')]
    )
    def test_move_doc(self, doc_num, shelf_num):
        result = move_doc(doc_num, shelf_num)
        if result is None:
            self.assertIsNone(result)
        else:
            self.assertIn(doc_num, result[shelf_num])

    @parameterized.expand(
        [['5'], ['1']]
    )
    def test_add_shelf(self, new_shelf):
        result = add_shelf(new_shelf)
        if result is None:
            self.assertIsNone(result)
        else:
            self.assertIn(new_shelf, result.keys())

    @patch('builtins.input', side_effect=['p', '2207 876234'])
    def test_main1(self, input_mock):
        result = main()
        self.assertEqual(people, result)

    @patch('builtins.input', side_effect=['a', 'passport', '22-123', 'Adam Smith', '1'])
    def test_main2(self, input_mock):
        result = main()
        self.assertEqual(add_new, result)

    @patch('builtins.input', side_effect=['as', '5'])
    def test_main3(self, input_mock):
        result = main()
        self.assertEqual(add_shelf, result)

    @patch('builtins.input', side_effect=['DD'])
    def test_main4(self, input_mock):
        result = main()
        self.assertEqual('dd', result)


if __name__ == '__main__':
    unittest.main()
