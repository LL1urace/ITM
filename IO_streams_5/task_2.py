# Практика:

# 2. Откройте и прочитайте данные с файла lorum.txt, способом, который рассматривается в видео из пункта 1.
import os

def file_read():
    base_dir = os.path.dirname(__file__)  # директория с файлом, где определена функция
    file_path = os.path.join(base_dir, 'files_task2/task_2/lorum.txt')
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content



if __name__ == "__main__":
    print(file_read())