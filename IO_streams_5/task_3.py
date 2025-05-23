# Практика:
from idlelib.outwin import file_line_progs

# 3. Прочитать про разницу между модами, при открытии файла
# https://stackoverflow.com/questions/1466000/difference-between-modes-a-a-w-w-and-r-in-built-in-open-function
# Попробуйте открыть файлы с разными значениями mode для чтения.
import os

def demonstrate_file_modes(base_dir="files/task_3"):
    os.makedirs(base_dir, exist_ok=True)

    with open(os.path.join(base_dir, "file_w.txt"), 'w') as file_w:
        file_w.write("Это файл в режиме 'w'\n")

    with open(os.path.join(base_dir, "file_wplus.txt"), 'w+') as file_wplus:
        file_wplus.write("Это файл в режиме 'w+'\n")
        file_wplus.seek(0)
        print(file_wplus.read())

    with open(os.path.join(base_dir, "file_a.txt"), 'a') as file_a:
        file_a.write("Добавлено в файл 'a'\n")

    with open(os.path.join(base_dir, "file_aplus.txt"), 'a+') as file_aplus:
        file_aplus.write("Добавлено в файл 'a+'\n")
        file_aplus.seek(0)
        print(file_aplus.read())

    try:
        with open(os.path.join(base_dir, "file_r.txt"), 'r') as file_r:
            print(file_r.read())
    except FileNotFoundError:
        print("Файл 'file_r.txt' не существует")

    try:
        with open(os.path.join(base_dir, "file_rplus.txt"), 'r+') as file_rplus:
            file_rplus.write("Это файл в режиме 'r+'\n")
    except FileNotFoundError:
        print("Файл 'file_rplus.txt' не существует")

if __name__ == "__main__":
    demonstrate_file_modes()