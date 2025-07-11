# Практика:
#
# 2. Напишите скрипт который создаст параллельно 10 файлов
# с именем `file_ {index}.txt' и записывает их номер внутрь файла.
import os
import time
import threading

# Создаем файл и записываем индекс внутрь
def create_file_with_index(index: int, folder: str = "files_task2") -> None:
    os.makedirs(folder, exist_ok=True)
    with open(f"{folder}/file_{index}.txt", "w", encoding="utf-8") as f:
        f.write(str(index))

def main():
    time_start = time.perf_counter()
    threads = []
    for i in range(10):
        task = threading.Thread(target=create_file_with_index, args=(i,), daemon=False)
        threads.append(task)
        task.start()

    for task in threads:
        task.join()

    time_end = time.perf_counter()
    print(f"Time: {time_end - time_start:.6f} seconds")



if __name__ == "__main__":
    main()