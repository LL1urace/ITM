# Практика:

# 2. Откройте и прочитайте данные с файла lorum.txt, способом, который рассматривается в видео из пункта 1.
def file_read():
    file = open('files/task_2/lorum.txt')
    print(file.read())
    file.close()



if __name__ == "__main__":
    file_read()