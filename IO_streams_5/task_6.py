# Практика:

# 6. Прочитайте статью и выполните действия, которые там указаны с файлом bikes.csv
# https://webtort.ru/чтение-csv-файла-в-python-при-помощи-pandas/
import pandas as pd
import pathlib


def read_bikes_csv(
        mode="all",
        nrows=None,
        skip_rows=None,
        show_info=True,
        file_path=None  # Добавлен параметр для пути к файлу
):
    """
    Чтение CSV-файла с разными режимами.

    :param file_path: путь к csv файлу. Если None — используется стандартный путь.
    """
    if file_path is None:
        work_path = pathlib.Path.cwd()
        data_path = pathlib.Path(work_path, 'files/task_6', "bikes.csv")
    else:
        data_path = pathlib.Path(file_path)

    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)

    if mode == "head":
        df = pd.read_csv(data_path)
        result = df.head(10)
    elif mode == "nrows":
        result = pd.read_csv(data_path, nrows=nrows)
    elif mode == "skip":
        result = pd.read_csv(data_path, skiprows=skip_rows)
    else:  # mode == "all"
        result = pd.read_csv(data_path)

    if show_info:
        print(result)

    return result


# Пример вызова
if __name__ == "__main__":
    # Прочитать всё
    read_bikes_csv(mode="all")

    # Прочитать первые 10 строк
    # read_bikes_csv(mode="head")

    # Прочитать 3 строки
    # read_bikes_csv(mode="nrows", nrows=3)

    # Пропустить строки с 1 по 2
    # read_bikes_csv(mode="skip", skip_rows=range(1, 3))