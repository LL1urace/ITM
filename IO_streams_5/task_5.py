# Практика:

# task_5_context_manager_examples.py
import os
import threading
import asyncio
from aiohttp import ClientSession

# 1. Ошибка: открытие файлов без закрытия
def demo_open_many_files_without_closing():
    lst = []
    for _ in range(10000):
        lst.append(open("files/task_5/passwords.txt", 'w'))  # вызовет ошибку на большой итерации

# 2. Без ошибки: закрытие вручную
def demo_open_many_files_with_closing():
    lst = []
    for _ in range(10000):
        f = open("files/task_5/passwords.txt", 'w')
        lst.append(f)
        f.close()
    return "OK"

# 3. Контекстный менеджер
def demo_write_with_context_manager(file_path="files/task_5/passwords.txt"):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('123\n')
        f.write('hello\n')
    return "Written successfully"

# 4. Много открытий через with
def demo_many_opens_with_context_manager():
    for _ in range(10000):
        with open("files/task_5/passwords.txt", 'w', encoding='utf-8') as f:
            f.write("test\n")
    return "OK"

# 5. Попытка использовать файл после выхода из with
def demo_write_after_context_error():
    with open("files/task_5/passwords.txt", 'w', encoding='utf-8') as f:
        f.write('hello\n')
    try:
        f.write('outside\n')  # ОШИБКА
    except ValueError as e:
        return f"Error: {e}"

# 6. Попытка записи в закрытый файл
def demo_write_closed_file_error():
    with open("files/task_5/passwords.txt", 'w', encoding='utf-8') as f:
        f.write('data\n')
    try:
        return f.write('123')  # ОШИБКА
    except ValueError as e:
        return f"Error: {e}"

# 7. Ошибка: print не поддерживает контекст
def demo_with_non_context_object():
    try:
        with print("files/task_5/passwords.txt", 'w') as f:
            f.write("test\n")
    except Exception as e:
        return f"Error: {e}"

# 8. Пример с os.scandir
def list_current_directory_files():
    result = []
    with os.scandir(".") as entries:
        for entry in entries:
            result.append((entry.name, entry.stat().st_size))
    return result

# 9. Пример с threading.Lock()
def demo_threading_lock_with_context():
    lock = threading.Lock()
    with lock:
        return "Lock acquired and released"

# 10. Асинхронный пример с aiohttp
async def fetch_python_org():
    async with ClientSession() as session:
        async with session.get("https://python.org") as response:
            status = response.status
            content_type = response.headers.get('content-type', 'N/A')
            html_preview = (await response.text())[:15]
            return status, content_type, html_preview

# -------------------- MAIN ----------------------
def main():
    print("Выберите функцию (введите номер):")
    options = {
        1: demo_open_many_files_without_closing,
        2: demo_open_many_files_with_closing,
        3: demo_write_with_context_manager,
        4: demo_many_opens_with_context_manager,
        5: demo_write_after_context_error,
        6: demo_write_closed_file_error,
        7: demo_with_non_context_object,
        8: list_current_directory_files,
        9: demo_threading_lock_with_context,
        10: lambda: asyncio.run(fetch_python_org()),
    }

    for i, func in options.items():
        print(f"{i}. {func.__name__}")

    try:
        choice = int(input("\nВведите номер: "))
        if choice in options:
            result = options[choice]()
            print("\nРезультат:", result)
        else:
            print("Неверный номер")
    except Exception as e:
        print(f"Ошибка при выполнении: {e}")



if __name__ == "__main__":
    main()