def combine_csv_files(file_part1, file_part2, output_file):
    """
    Функция для объединения двух CSV-файлов в один.

    :param file_part1: Путь к первому файлу.
    :param file_part2: Путь ко второму файлу.
    :param output_file: Путь для сохранения объединенного файла.
    """
    # Чтение первого файла
    with open(file_part1, 'r') as f:
        data_part1 = f.readlines()

    # Чтение второго файла
    with open(file_part2, 'r') as f:
        data_part2 = f.readlines()

    # Объединение данных из двух файлов
    combined_data = data_part1 + data_part2

    # Запись объединенных данных в новый файл
    with open(output_file, 'w') as f:
        f.writelines(combined_data)

    print(f"Файлы {file_part1} и {file_part2} успешно объединены в {output_file}")

combine_csv_files('data/mnist_train_1.csv', 'data/mnist_train_2.csv', 'data/mnist_train.csv')
