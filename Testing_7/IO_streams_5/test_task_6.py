import pytest
from IO_streams_5.task_6 import read_bikes_csv
import pytest



@pytest.fixture
def sample_csv(tmp_path):
    # Создаем временный csv файл с тестовыми данными
    csv_path = tmp_path / "bikes.csv"
    csv_content = """id,model,price
1,Roadster,1000
2,Mountain,1500
3,Hybrid,1200
4,BMX,800
"""
    csv_path.write_text(csv_content, encoding="utf-8")
    return csv_path

def test_read_all(sample_csv):
    result = read_bikes_csv(file_path=str(sample_csv), mode="all")
    # Проверяем, что прочитали все строки, например, возвращается DataFrame или список строк
    assert len(result) == 4

def test_read_head(sample_csv):
    result = read_bikes_csv(file_path=str(sample_csv), mode="head")
    assert len(result) == 10 or len(result) == 4  # если в файле меньше 10 строк

def test_read_nrows(sample_csv):
    result = read_bikes_csv(file_path=str(sample_csv), mode="nrows", nrows=3)
    assert len(result) == 3

def test_skip_rows(sample_csv):
    result = read_bikes_csv(file_path=str(sample_csv), mode="skip", skip_rows=range(1, 3))
    # Проверяем, что пропущены строки 1 и 2 (нумерация с 0 или 1 зависит от реализации)
    # Например, если пропущены 2 строки, размер меньше на 2
    assert len(result) == 2