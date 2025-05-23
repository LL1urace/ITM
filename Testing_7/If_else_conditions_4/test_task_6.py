import pytest
from If_else_conditions_4.task_6 import define_score


@pytest.mark.parametrize(
    ("user_input", "expected_output"),
    [
        ("1", "Ваша оценка: «плохо»\n"),
        ("2", "Ваша оценка: «неудовлетворительно»\n"),
        ("3", "Ваша оценка: «удовлетворительно»\n"),
        ("4", "Ваша оценка: «хорошо»\n"),
        ("5", "Ваша оценка: «отлично»\n"),
        ("0", "Ошибка-ввода: K не находится в диапазоне 1-5\n"),
        ("abc", "Ошибка-ввода: K не является целым числом\n"),
    ]
)
def test_define_score(monkeypatch, capsys, user_input, expected_output):
    # Подменяем input, чтобы вернуть user_input
    monkeypatch.setattr("builtins.input", lambda _: user_input)

    define_score()
    # Захватываем вывод print
    captured = capsys.readouterr()
    assert captured.out == expected_output