import os


def get_file_properties():
    file_path = os.path.abspath(__file__)  # Получаем путь к текущему файлу
    dir_path = os.path.dirname(file_path)  # Получаем путь к папке
    files = os.listdir(dir_path)  # Получаем список файлов в папке

    if files:
        first_file = os.path.join(dir_path, files[0])  # Берем первый файл в папке
        file_stats = os.stat(first_file)

        with open('inf.txt', 'w') as file:
            file.write(f"Имя файла: {files[0]}\n")
            file.write(f"Размер файла: {file_stats.st_size} байт\n")
            file.write(f"Дата последнего изменения: {file_stats.st_mtime}\n")
    else:
        print("В папке нет файлов.")


get_file_properties()