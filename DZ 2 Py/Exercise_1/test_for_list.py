import pytest


# Проверяю возможность очистки списка
def test_list_1(list_test):
    assert list_test.clear() == None


# Проверяю возможность добавления новых элементов
def test_list_2(list_test):
    p = len(list_test)
    list_test.append("el_1")
    new = len(list_test)
    assert new == p+1


# Тест проверки добавления элемента в список и сравнение его длины
@pytest.mark.parametrize('item', [1, 2, 3])
def test_list_3(list_test, item):
    list_test.append(item)
    print(list_test)
    assert item in list_test


# Проверяю наличие требуемого мне элемента
def test_list_4(list_test):
    assert list_test.index("a") == 3


# Проверяем возможность сделать копию списка
def test_list_5(list_test):
    p = list_test.copy()
    assert p == list_test