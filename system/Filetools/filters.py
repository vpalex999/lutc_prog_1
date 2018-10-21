import sys

def filter_files(name, function):       # фильтрация файлов через функцию
    input = open(name, 'r')             # создать объекты файлов
    output = open(name + '.out', 'w')   # выходной файл

    for line in input:
        output.write(function(line))    # записать изменённую строку
    
    input.close()
    output.close()  # выходной файл имеет расширение '.out'


# с менеджером контекста
def filter_files_2(name, function):     # фильтрация файлов через функцию
    with open(name, 'r') as input, open(name + '.out', 'w') as output:
        for line in input:
            output.write(function(line))    # записать изменённую строку


def filter_stream(function):        # отсутствуют явные файлы
    while True:                     # использовать стандартные потоки
        line = sys.stdin.readline() # или: input()
        if not line: break
        print(function(line), end='')   # или: sys.stdout.write()


# с применением итераторов объектов файлов
def filter_stream_2(function):        # отсутствуют явные файлы
    for line in sys.stdin:            # использовать стандартные потоки
        print(function(line), end='') # или: sys.stdout.write()


if __name__ == '__main__':
    filter_stream(lambda line: line)    # копировать stdin в stdout, если
                                        # запущен как самостоятельный сценарий
