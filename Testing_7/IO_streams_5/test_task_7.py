import pytest
from IO_streams_5.task_7 import sum_column_from_csv



def test_sum_column_from_csv(tmp_path):
    # Создаём временный CSV-файл с тестовыми данными
    csv_content = """Rachel1,Rachel2
10,100
20,200
30,300
"""
    test_csv = tmp_path / "test_bikes.csv"
    test_csv.write_text(csv_content, encoding="utf-8")

    # Вызываем функцию с тестовым файлом
    result = sum_column_from_csv(file_path=test_csv, column_name='Rachel1')

    # Проверяем, что сумма посчитана правильно: 10+20+30 = 60
    assert result == 60
