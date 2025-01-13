from yandex_testing_lesson import Rectangle
import pytest


def test_negative1():
    with pytest.raises(ValueError):
        Rectangle(-1, 2)


def test_negative2():
    with pytest.raises(ValueError):
        Rectangle(-2, 1)


def test_str1():
    with pytest.raises(TypeError):
        Rectangle('1', 2)


def test_str2():
    with pytest.raises(TypeError):
        Rectangle(1, '2')


def test_list1():
    with pytest.raises(TypeError):
        Rectangle([1], 2)


def test_list2():
    with pytest.raises(TypeError):
        Rectangle(1, [2])


def test_area():
    assert Rectangle(2, 2).get_area() == 4


def test_area_zero():
    assert Rectangle(0, 2).get_area() == 0


def test_perimeter():
    assert Rectangle(5, 1).get_perimeter() == 12
