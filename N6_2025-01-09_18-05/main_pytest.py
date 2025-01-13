from yandex_testing_lesson import reverse
import pytest


def test_reverse():
    assert reverse('asdf') == "fdsa"


def test_wrong_type():
    with pytest.raises(TypeError):
        reverse(1)


def test_empty():
    assert reverse('') == ''


def test_char():
    assert reverse('a') == 'a'


def test_palindrome():
    assert reverse('шалаш') == 'шалаш'


def test_string():
    assert reverse('qwerty') == 'ytrewq'


def test_wrong_type_iter():
    with pytest.raises(TypeError):
        reverse([1, 2, 3])
