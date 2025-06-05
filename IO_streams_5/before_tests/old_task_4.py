# Практика:

# 4. Запишите любую информацию в файл с разными значениями mode для записи.
# Какую разницу при записи файла вы заметили?

# 1) mode r (Ошибка если файл не существует/Ошибка, неподдерживаемая операция)
# file_r = open("files_task2/task_4/file_r.txt", 'r', encoding="utf-8") # r
# file_r.write("Файл r")
# file_r.close()


# 2) mode r+ (Ошибка если файл не существует/Запись в начало файла/Перезапись поверх существующего)
# file_rplus = open("files_task2/task_4/file_rplus.txt", 'r+', encoding="utf-8") # r+
# file_rplus.write("Файл rplus")
# file_rplus.close()


# 3) mode w (Запись в начало файла/Перезапись файла полностью)
# file_w = open("files_task2/task_4/file_w.txt", 'w', encoding="utf-8") # w
# file_w.write("Файл w")
# file_w.close()


# 4) mode w+ (Запись в начало файла/Перезапись файла полностью)
# file_wplus = open("files_task2/task_4/file_wplus.txt", 'w+', encoding="utf-8") # w+
# file_wplus.write("Файл wplus")
# file_wplus.close()


# 5) mode a (Запись в конец файла/Продолжает запись в файл не стирая содержимое)
# file_a = open("files_task2/task_4/file_a.txt", 'a', encoding="utf-8") # a
# file_a.write("Файл a")
# file_a.close()


# 6) mode a+ (Запись в конец файла/Продолжает запись в файл не стирая содержимое)
# file_aplus = open("files_task2/task_4/file_aplus.txt", 'a+', encoding="utf-8") # a+
# file_aplus.write("Файл aplus")
# file_aplus.close()