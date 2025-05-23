# Практика:

# 7. Посчитайте сумму столбца Rachel1 из файла bikes.csv
import pandas as pd
import pathlib

work_path = pathlib.Path.cwd()
data_path = pathlib.Path(work_path, 'files/task_7', "bikes.csv")

def sum_column_from_csv(file_path=None, column_name='Rachel1'):
    if file_path is None:
        work_path = pathlib.Path.cwd()
        file_path = pathlib.Path(work_path, 'files/task_7', "bikes.csv")

    data = pd.read_csv(file_path)
    column_data = data[column_name]
    column_sum = column_data.sum()
    print(column_sum)
    return column_sum



if __name__ == "__main__":
    sum_column_from_csv()