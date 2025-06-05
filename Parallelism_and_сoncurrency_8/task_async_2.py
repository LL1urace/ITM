# Практика:
#
# 2. Напишите скрипт который создаст параллельно 10 файлов
# с именем `file_ {index}.txt' и записывает их номер внутрь файла.
import time
import threading

# Создаем файл и записываем индекс внутрь
def create_file_with_index(index: int) -> None:
    with open(f"files_task2/file_{index}.txt", "w", encoding="utf-8") as f:
        f.write(str(index))


if __name__ == "__main__":
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