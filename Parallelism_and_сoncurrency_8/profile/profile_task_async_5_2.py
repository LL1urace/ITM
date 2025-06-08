# Практика:
#
# 5. Выполните профилирование для определения точек потребления памяти и просадок по времени.
import os
import time
import threading
import cProfile
import pstats
from memory_profiler import profile



# Task №2
# Создаем файл и записываем индекс внутрь
def create_file_with_index(index: int, folder: str = "files_task2") -> None:
    os.makedirs(folder, exist_ok=True)
    with open(f"{folder}/file_{index}.txt", "w", encoding="utf-8") as f:
        f.write(str(index))


@profile
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
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()
    stats = pstats.Stats(profiler)
    stats.strip_dirs()
    stats.sort_stats('cumtime')
    stats.print_stats(15)