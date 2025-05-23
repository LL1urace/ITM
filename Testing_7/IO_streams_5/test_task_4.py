import os
import tempfile
import pytest
from IO_streams_5.task_4 import file_write_modes_testing



@pytest.fixture
def temp_dir():
    with tempfile.TemporaryDirectory() as tmpdirname:
        yield tmpdirname


def test_file_write_modes(temp_dir):
    results = file_write_modes_testing(temp_dir)

    # 1. Проверяем, что все ключи присутствуют
    expected_modes = {"r", "r+", "w", "w+", "a", "a+"}
    assert set(results.keys()) == expected_modes, "Не все режимы присутствуют в результатах"

    # 2. Проверка на ошибки в 'r' и 'r+'
    assert "Ошибка" in results["r"], "Режим 'r' должен выдать ошибку при отсутствии файла"
    assert "Ошибка" in results["r+"], "Режим 'r+' должен выдать ошибку при отсутствии файла"

    # 3. Остальные режимы должны отработать успешно
    for mode in ["w", "w+", "a", "a+"]:
        assert results[mode] == "OK", f"Режим '{mode}' должен работать без ошибок"

    # 4. Проверка, что нужные файлы реально созданы
    for filename in ["file_w.txt", "file_wplus.txt", "file_a.txt", "file_aplus.txt"]:
        path = os.path.join(temp_dir, filename)
        assert os.path.exists(path), f"Файл {filename} должен быть создан"
