from yandex_testing_lesson import is_under_queen_attack
import pytest


def test_type_error1():
    with pytest.raises(TypeError):
        is_under_queen_attack(None, "a3")
    with pytest.raises(TypeError):
        is_under_queen_attack(True, "a3")
    with pytest.raises(TypeError):
        is_under_queen_attack(1, 'a2')
    with pytest.raises(TypeError):
        is_under_queen_attack('b3', 2)
    with pytest.raises(TypeError):
        is_under_queen_attack([1], 'a2')
    with pytest.raises(TypeError):
        is_under_queen_attack('b3', (2,))
    with pytest.raises(TypeError):
        is_under_queen_attack("e2", None)
    with pytest.raises(TypeError):
        is_under_queen_attack("e2", False)


def test_value_error():
    with pytest.raises(ValueError):
        is_under_queen_attack('j2', 'a1')
    with pytest.raises(ValueError):
        is_under_queen_attack('b2', 'a9')
    with pytest.raises(ValueError):
        is_under_queen_attack('jbc', 'a1')
    with pytest.raises(ValueError):
        is_under_queen_attack('', 'a1')
    with pytest.raises(ValueError):
        is_under_queen_attack("j5", "e4")
    with pytest.raises(ValueError):
        is_under_queen_attack("55", "a4")
    with pytest.raises(ValueError):
        is_under_queen_attack("a0", "h8")
    with pytest.raises(ValueError):
        is_under_queen_attack("A0", "h8")
    with pytest.raises(ValueError):
        is_under_queen_attack('b2', 'aboba')
    with pytest.raises(ValueError):
        is_under_queen_attack('1a', 'a2')
    with pytest.raises(ValueError):
        is_under_queen_attack('b2', '3d')
    with pytest.raises(ValueError):
        is_under_queen_attack('b2', '4D')
    with pytest.raises(ValueError):
        is_under_queen_attack("d4", "i9")
    with pytest.raises(ValueError):
        is_under_queen_attack("b4", "22")
    with pytest.raises(ValueError):
        is_under_queen_attack("b4", "")


def test_column1():
    assert is_under_queen_attack('a2', 'c2')
    assert is_under_queen_attack('a2', 'd3') is False


def test_line():
    assert is_under_queen_attack('a7', 'a3')
    assert is_under_queen_attack('g5', 'a3') is False


def test_diag():
    assert is_under_queen_attack('a1', 'b2')
    assert is_under_queen_attack('a2', 'g3') is False
    assert is_under_queen_attack('c3', 'b2')
    assert is_under_queen_attack('d2', 'c3')
    assert is_under_queen_attack("c3", "a1")
    assert is_under_queen_attack("b2", "d4")


def test_edge():
    assert is_under_queen_attack("a1", "h8")
    assert is_under_queen_attack("a8", "h8")
    assert is_under_queen_attack("a8", "h1")
    assert is_under_queen_attack("a1", "h1")


def test_same_pos():
    assert is_under_queen_attack('f3', 'f3')

