import pytest
from yandex_testing_lesson import count_chars


def test_char():
    assert count_chars('a') == {'a': 1}


def test_string():
    assert count_chars('stringy string') == {
        's': 2,
        't': 2,
        'r': 2,
        'i': 2,
        'n': 2,
        'g': 2,
        'y': 1,
        ' ': 1,
    }


def test_empty():
    assert count_chars('') == {}


def test_type():
    with pytest.raises(TypeError):
        count_chars(1501)
