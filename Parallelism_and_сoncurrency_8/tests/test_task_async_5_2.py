# Практика:
#
# 5. Перекройте тестами выше указанные задачи.
import pytest
from Parallelism_and_сoncurrency_8 import task_async_2



# Task №2 (create_file_with_index, main)
# create_file_with_index
# Файл существует и содержимое правильное
@pytest.mark.parametrize("index", [0, 6, 75, -222, "stroka"])
def test_create_file_with_index(tmp_path, index):
    tmp_folder = tmp_path / "files_task2"
    task_async_2.create_file_with_index(index, str(tmp_folder))
    expected_file = tmp_folder / f"file_{index}.txt"
    assert expected_file.exists()

    with open(expected_file, encoding="utf-8") as f:
        text = f.read()
        assert text == str(index)


# main
# Стандартная работа main
def test_main_task_2(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    task_async_2.main()
    for i in range(10):
        file_path = tmp_path / "files_task2" / f"file_{i}.txt"
        assert file_path.exists()