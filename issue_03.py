import unittest
from one_hot_encoder import fit_transform
from pprint import pprint


class TestFitTransform(unittest.TestCase):
    def test_cities(self):
        '''
        Данный тест проверяет, правильно ли работает функция
        на тестовом примере
        '''
        CITIES = ['Moscow', 'New York', 'Moscow', 'London']
        actual = fit_transform(CITIES)
        expected = [('Moscow', [0, 0, 1]),
                    ('New York', [0, 1, 0]),
                    ('Moscow', [0, 0, 1]),
                    ('London', [1, 0, 0])]
        self.assertEqual(actual, expected)

    def test_alphabet_in(self):
        '''
        Данный тест проверяет, правильно ли работает функция
        при вызове метода assertIn
        '''
        ALFABET = ['A', 'B']
        actual = fit_transform(ALFABET)
        expected = [
            [('A', [1, 0]), ('B', [0, 1])],
            [('A', [0, 1]), ('B', [1, 0])],
        ]
        self.assertIn(actual, expected)

    def test_alphabet_equal(self):
        '''
        Данный тест проверяет, правильно ли работает функция
        при вызове метода assertEqual
        '''
        ALFABET1 = ['A', 'B', 'C']
        actual = fit_transform(ALFABET1)
        expected = [
            ('A', [0, 0, 1]),
            ('B', [0, 1, 0]),
            ('C', [1, 0, 0])
        ]
        self.assertEqual(actual, expected)

    def test_exception(self):
        '''
        Данный тест проверяет правильную работу функции при
        выбрасывании исключения
        '''
        with self.assertRaises(TypeError):
            fit_transform(1)


if __name__ == '__main__':
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    exp_transformed_cities = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    transformed_cities = fit_transform(cities)
    pprint(transformed_cities)
    assert transformed_cities == exp_transformed_cities
