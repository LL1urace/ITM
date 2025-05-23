import pytest
import os
import tempfile
from IO_streams_5.task_3 import demonstrate_file_modes



@pytest.fixture
def temp_dir():
    with tempfile.TemporaryDirectory() as tmpdirname:
        yield tmpdirname  # передаём временную директорию в тест
        # файлы будут автоматически удалены после теста

def read_file_content(path):
    with open(path, 'r', encoding='cp1251') as f:
        return f.read()

def test_demonstrate_file_modes(temp_dir):
    demonstrate_file_modes(temp_dir)

    files = {
        "file_w.txt": "Это файл в режиме 'w'\n",
        "file_wplus.txt": "Это файл в режиме 'w+'\n",
        "file_a.txt": "Добавлено в файл 'a'\n",
        "file_aplus.txt": "Добавлено в файл 'a+'\n",
    }

    # Проверяем содержимое файлов
    for filename, expected_content in files.items():
        path = os.path.join(temp_dir, filename)
        assert os.path.exists(path), f"Файл {filename} должен существовать"
        content = read_file_content(path)
        assert expected_content in content, f"Ожидалось, что файл {filename} содержит: {expected_content}"

    # Проверяем, что файлы, открываемые в 'r' и 'r+' режимах, не созданы
    assert not os.path.exists(os.path.join(temp_dir, "file_r.txt")), "'file_r.txt' не должен существовать"
    assert not os.path.exists(os.path.join(temp_dir, "file_rplus.txt")), "'file_rplus.txt' не должен существовать"