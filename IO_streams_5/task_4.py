# Практика:

# 4. Запишите любую информацию в файл с разными значениями mode для записи.
# Какую разницу при записи файла вы заметили?
import os



def file_write_modes_testing(base_dir="files_task2/task_4"):
    os.makedirs(base_dir, exist_ok=True)

    results = {}
    # 1) mode 'r'
    try:
        with open(os.path.join(base_dir, "file_r.txt"), 'r', encoding="utf-8") as f:
            f.write("Файл r")
        results["r"] = "OK"
    except Exception as e:
        results["r"] = f"Ошибка: {e}"

    # 2) mode 'r+'
    try:
        with open(os.path.join(base_dir, "file_rplus.txt"), 'r+', encoding="utf-8") as f:
            f.write("Файл rplus")
        results["r+"] = "OK"
    except Exception as e:
        results["r+"] = f"Ошибка: {e}"

    # 3) mode 'w'
    try:
        with open(os.path.join(base_dir, "file_w.txt"), 'w', encoding="utf-8") as f:
            f.write("Файл w")
        results["w"] = "OK"
    except Exception as e:
        results["w"] = f"Ошибка: {e}"

    # 4) mode 'w+'
    try:
        with open(os.path.join(base_dir, "file_wplus.txt"), 'w+', encoding="utf-8") as f:
            f.write("Файл wplus")
        results["w+"] = "OK"
    except Exception as e:
        results["w+"] = f"Ошибка: {e}"

    # 5) mode 'a'
    try:
        with open(os.path.join(base_dir, "file_a.txt"), 'a', encoding="utf-8") as f:
            f.write("Файл a")
        results["a"] = "OK"
    except Exception as e:
        results["a"] = f"Ошибка: {e}"

    # 6) mode 'a+'
    try:
        with open(os.path.join(base_dir, "file_aplus.txt"), 'a+', encoding="utf-8") as f:
            f.write("Файл aplus")
        results["a+"] = "OK"
    except Exception as e:
        results["a+"] = f"Ошибка: {e}"

    return results

# Пример вызова:
if __name__ == "__main__":
    res = file_write_modes_testing()
    for mode, status in res.items():
        print(f"Режим '{mode}': {status}")