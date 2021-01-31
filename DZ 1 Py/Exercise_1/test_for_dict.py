import pytest


# Проверяем возможность очистки всего словаря
def test_dict_1(dict_test):
    assert dict_test.clear() == None


# Удаление элемента словаря по ключу
@pytest.mark.parametrize('key', ["index"])
def test_dict_2(dict_test, key):
    dict_test.pop(key)
    assert key not in dict_test


# Добавление пары key-value
def test_dict_3(dict_test):
    q = len(dict_test)
    dict_test.update({"test": True})
    assert len(dict_test) == q+1


# Копирование словаря
def test_dict_4(dict_test):
    c = dict_test.copy()
    assert dict_test == c


# Возвращаем ключи в словаре
def test_dict_5(dict_test):
    key = dict_test.keys()
    assert "index" in key