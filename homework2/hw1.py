# Работа с файлами
# Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
# Подсчитайте количество слов в тексте
# Замените точки в тексте на восклицательные знаки
# Сохраните результат в файл referat2.txt

read_file_name = 'referat.txt'
write_file_name = 'referat2.txt'

with open(read_file_name, 'r', encoding='utf-8') as file:
    content = file.read()
    file_len = len(content)
    print(f'Длина файла {read_file_name} в символах: {file_len}')

    file_words_count = len(content.split())
    print(f'Количество слов файла {read_file_name}: {file_words_count}')

