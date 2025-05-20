# Практика:
from idlelib.outwin import file_line_progs

# 3. Прочитать про разницу между модами, при открытии файла
# https://stackoverflow.com/questions/1466000/difference-between-modes-a-a-w-w-and-r-in-built-in-open-function
# Попробуйте открыть файлы с разными значениями mode для чтения.

# r и r+ выдают ошибки так как требуют чтобы файл существовал
# file_r = open("files/task_3/file_r.txt", 'r') # r
# file_rplus = open("files/task_3/file_rplus.txt", 'r+') # r+

# остальные создают новый файл в указанной директории
file_w = open("files/task_3/file_w.txt", 'w') # w
file_wplus = open("files/task_3/file_wplus.txt", 'w+') # w+
file_a = open("files/task_3/file_a.txt", 'a') # a
file_aplus = open("files/task_3/file_aplus.txt", 'a+') # a+