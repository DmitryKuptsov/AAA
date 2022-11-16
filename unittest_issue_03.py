from typing import List, Tuple
import unittest


def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError('expected at least 1 arguments, got 0')

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f'{{0:0{len(uniq_categories)}b}}'

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (int(b) for b in bin_format.format(1 << len(
                                                          seen_categories)))
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows


class TestFitTransform(unittest.TestCase):
    def test_cities(self):
        CITIES = ['Moscow', 'New York', 'Moscow', 'London']
        actual = fit_transform(CITIES)
        expected = [('Moscow', [0, 0, 1]),
                    ('New York', [0, 1, 0]),
                    ('Moscow', [0, 0, 1]),
                    ('London', [1, 0, 0])]
        self.assertEqual(actual, expected)

    def test_al(self):
        AL = ['A', 'B']
        actual = fit_transform(AL)
        expected = [[('A', [1, 0]),
                    ('B', [0, 1])], [('A', [0, 1]),
                    ('B', [1, 0])]]
        self.assertIn(actual, expected)

    def test_al1(self):
        AL1 = ['A', 'B', 'C']
        actual = fit_transform(AL1)
        expected = [('A', [1, 0, 0]),
                    ('B', [0, 1, 0]),
                    ('C', [0, 0, 1])]
        self.assertEqual(actual, expected)

    def test_al1_wr(self):
        AL1Wr = []
        actual = fit_transform(AL1Wr)
        self.assertRaises(TypeError, actual)


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
