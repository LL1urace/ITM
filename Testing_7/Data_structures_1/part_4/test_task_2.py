import pytest
from Data_structures_1.part_4.task_2 import fix_city_name

# --- Основной корректный кейс ---
def test_fix_city_name_standard():
    r = ["Ростов", "+", "на", "-", "Дону"]
    result = fix_city_name(r.copy())
    assert result == "Ростов-на-Дону"

# --- Проверка, что второй элемент стал '-' ---
def test_fix_city_name_modifies_index_1():
    r = ["Город", "+", "в", "центре", "РФ"]
    fix_city_name(r)
    assert r[1] == "-"

# --- Проверка, что функция обрезает до 5 элементов и собирает строку ---
def test_fix_city_name_shortens_to_five():
    r = ["А", "+", "Б", "В", "Г", "лишнее"]
    result = fix_city_name(r.copy())
    assert result == "А-БВГ"

# --- Ошибка при недостаточной длине списка ---
def test_fix_city_name_too_short():
    r = ["Мало", "+"]
    with pytest.raises(IndexError):
        fix_city_name(r)

# --- Ошибка, если список не изменяемый ---
def test_fix_city_name_immutable_input():
    r = ("А", "+", "Б", "В", "Г")
    with pytest.raises(TypeError):
        fix_city_name(r)