import pytest


# Добавление элементов в множества
@pytest.mark.parametrize('ell', {"weapon", "armor"})
def test_set_1(set_test_1, ell):
    set_test_1.add(ell)
    assert ell in set_test_1


# Удаление элементов
@pytest.mark.parametrize('ell', {"weapon", "armor"})
def test_set_1(set_test_1, ell):
    set_test_1.add(ell)
    assert ell in set_test_1


# Создаем копию множества
def test_set_3(set_test_1):
    i = set_test_1.copy()
    assert i == set_test_1


# Объединение двух множеств
def test_set_4(set_test_1, set_test_2):
    i = set_test_1.update(set_test_2)
    assert set_test_1, set_test_2 in i


# Очистка множества
def test_set_5(set_test_1):
    set_test_1.clear()
    assert set_test_1.clear() == None
