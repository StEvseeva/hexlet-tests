from scripts.main import capitalize

if capitalize('hello') != 'Hello':
    # Выбрасываем исключение и завершаем выполнение теста
    raise Exception('Функция работает неверно!')

if capitalize('') != '':
    raise Exception('Функция работает неверно!')

print('Все тесты пройдены!')
