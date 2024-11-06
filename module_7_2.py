def custom_write(file_name, strings):
    # Открываем файл в режиме записи с поддержкой кодировки UTF-8
    file = open(file_name, mode='w', encoding='utf-8')
    strings_positions = {}

    # Проходимся по каждой строке в списке
    i = 1  # Начинаем счетчик строк с 1
    for string in strings:

        position = file.tell()  # Получаем текущую позицию курсора в файле
        file.write(string + '\n') # Записываем строку в файл
        strings_positions[(i, position)] = string # Добавляем запись в словарь
        """ (i, position) — это кортеж, состоящий из двух значений:
          i — это номер текущей строки, а position — позиция
           в файле, с которой начинается данная строка.
           Кортеж используется в качестве ключа в словаре.

        string — это сама строка, которую нужно записать в файл.
           Она становится значением, соответствующим ключу (i, position).

          То есть в результате в словарь добавляется новая пара «ключ - значение»,
           где ключом является кортеж(i, position), а значением — строка string.

           Например, если i = 1 и position = 0, 
           а строка равна "Text for tell.", то
           в словарь добавится следующая запись:

           strings_positions[(1, 0)] = "Text for tell." 
           """


        i += 1 # Увеличиваем счетчик строк

    file.close() # Закрываем файл после всех операций
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

