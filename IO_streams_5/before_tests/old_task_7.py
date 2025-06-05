# Практика:

# 7. Посчитайте сумму столбца Rachel1 из файла bikes.csv
import pandas as pd
import pathlib

work_path = pathlib.Path.cwd()
data_path = pathlib.Path(work_path, 'files_task2/task_7', "bikes.csv")

def sum_column_from_csv():
    data = pd.read_csv(data_path)
    column_data = data['Rachel1']
    column_sum = column_data.sum()
    print(column_sum)


sum_column_from_csv()