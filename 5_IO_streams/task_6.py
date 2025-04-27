# Практика:

# 6. Прочитайте статью и выполните действия, которые там указаны с файлом bikes.csv
# https://webtort.ru/чтение-csv-файла-в-python-при-помощи-pandas/
import pandas as pd
import pathlib

work_path = pathlib.Path.cwd()
data_path = pathlib.Path(work_path, 'files/task_6', "bikes.csv")

pd.set_option('display.max_columns', None)  # Показывать все столбцы
pd.set_option('display.width', None) # Не ограничивать ширину вывода


# data = pd.read_csv(data_path, header=0) # header=None - если нет заголовков
# print(data.head(10))


# data = pd.read_csv(data_path, nrows=3)
# print(data)


# data = pd.read_csv(data_path, header=0, skiprows=range(1, 3))
# print(data)


data = pd.read_csv(data_path)
print(data)