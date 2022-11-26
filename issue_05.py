from unittest.mock import patch
from io import StringIO
import pytest
from what_year_is_now import what_is_year_now


def test_first_type():
    '''
    Данный тест проверяет, правильно ли функция работает с форматом первого
    типа (DD.MM.YYYY)
    '''
    with patch('what_year_is_now.urllib.request.urlopen',
               return_value=StringIO(
            initial_value='{"currentDateTime":"01.03.2019"}')):
        assert 2019 == what_is_year_now()


def test_second_type():
    '''
    Данный тест проверяет, правильно ли функция работает с форматом второго
    типа (YYYY-MM-DD)
    '''
    with patch('what_year_is_now.urllib.request.urlopen',
               return_value=StringIO(
            initial_value='{"currentDateTime":"2019-01-01"}')):
        assert 2019 == what_is_year_now()


def test_error():
    '''
    Данный тест проверяет, правильно ли функция работает с исключениями
    '''
    with patch('what_year_is_now.urllib.request.urlopen',
               return_value=StringIO(
            initial_value='{"currentDateTime":"2019.00.00"}')):
        with pytest.raises(ValueError):
            what_is_year_now()
