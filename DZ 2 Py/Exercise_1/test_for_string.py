import pytest


# Проверяем конкатенацию
def test_string_1(string_1, string_2):
    i = string_1 + string_2
    assert string_1, string_2 in i


# Проверяем длину строки
def test_string_2(string_1):
    h = len(string_1)
    assert h == 13


# Проверяем начинаюися ли слова в строке с заглавной буквы
def test_string_3(string_1):
    i = string_1.istitle()
    assert i == False


# Увеличиваем длину строки
@pytest.mark.parametrize("simbol", ["1", "2", "3"])
def test_string_4(string_1, simbol):
    h = len(string_1)
    a = string_1.ljust(14, simbol)
    i = len(a)
    assert i == h+1


# Проверяем возможность сделать все буквы заглавными/ форматировать текст
def test_string_5(string_1):
    a = string_1.upper()
    assert a != string_1
















                         
