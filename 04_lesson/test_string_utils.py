import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("hello", "hello"),
    ("   много пробелов", "много пробелов"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    (" ", ""),
    ("  ", ""),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "k", True),
    ("Hello", "o", True),
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", False),
    ("", "a", False),
    ("abc", "d", False),
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("Hello", "l", "Heo"),
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "z", "SkyPro"),   # символа нет — строка не меняется
    ("", "a", ""),
    ("abc", "", "abc"),          # пустой символ для удаления
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected

def test_capitalize_none():
    with pytest.raises(AttributeError):
        string_utils.capitalize(None)

def test_trim_none():
    with pytest.raises(AttributeError):
        string_utils.trim(None)

def test_contains_none():
    with pytest.raises(AttributeError):
        string_utils.contains(None, "a")

def test_delete_symbol_none():
    with pytest.raises(AttributeError):
        string_utils.delete_symbol(None, "a")

def test_trim_with_tab():    
    assert string_utils.trim("\tskypro") == "skypro"  # Ожидаем "skypro", но получим "\tskypro"

def test_delete_symbol_empty_symbol():
    assert string_utils.delete_symbol("abc", "") == "abc"  # Ожидаем "abc", но получим ""

def test_contains_empty_string():
    assert string_utils.contains("abc", "") == True

def test_capitalize_single_char():
    assert string_utils.capitalize("a") == "A"