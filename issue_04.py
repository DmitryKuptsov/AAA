import pytest
from one_hot_encoder import fit_transform


def test_cities():
    '''
    Данный тест проверяет работу функции на тестовом примере
    '''
    CITIES = ['Moscow', 'New York', 'Moscow', 'London']
    actual = fit_transform(CITIES)
    expected = [('Moscow', [0, 0, 1]),
                ('New York', [0, 1, 0]),
                ('Moscow', [0, 0, 1]),
                ('London', [1, 0, 0])]
    assert actual == expected


def test_alphabet():
    '''
    Данный тест проверяет, правильно ли работает функция
    при проверке нескольких вариантов
    '''
    ALFABET = ['A', 'B']
    actual = fit_transform(ALFABET)
    expected1 = [('A', [1, 0]),
                 ('B', [0, 1])]
    expected2 = [('A', [0, 1]),
                 ('B', [1, 0])]
    assert actual == expected1 or actual == expected2


def test_alphabet_not_equal():
    '''
    Данный тест проверяет, правильно ли работает функция
    при проверке на неравенство
    '''
    ALFABET1 = ['A', 'B', 'C']
    actual = fit_transform(ALFABET1)
    expected = [('A', [0, 0, 0]),
                ('B', [0, 0, 0]),
                ('C', [0, 0, 0])]
    assert actual != expected


def test_exception():
    '''
    Данный тест проверяет, правильно ли работает функция
    при получении исключения
    '''
    with pytest.raises(TypeError):
        fit_transform()


if __name__ == '__main__':
    from pprint import pprint

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
