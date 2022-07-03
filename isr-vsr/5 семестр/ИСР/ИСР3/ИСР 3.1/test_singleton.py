from main import CurrenciesList

if __name__ == '__main__':

    import unittest

    class TestPrecisionFunc(unittest.TestCase):

        def test_is_singleton(self):
            # проверка синглтона
            # если id объектов одинаковые, то декоратор-синглтон работает правильно
            my_cur_list = CurrenciesList()
            my_cur_list2 = CurrenciesList()
            my_cur_list2.get_currencies(["R01090B", "R01720", "R01565"])

            self.assertEqual(id(my_cur_list), id(my_cur_list2))
            
        def test_result_type(self):
            cur_list = CurrenciesList()
            self.assertIsInstance(cur_list.get_currencies(), dict)

    unittest.main(verbosity=1)  # закомментировать эту строчку, если тестируете в PyCharm
