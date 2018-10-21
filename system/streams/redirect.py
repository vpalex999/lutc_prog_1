"""
объекты, похожие на файлы, один из которых сохраняет в строке текст,
отправленный в стандартный поток вывода, а другой обеспечивает ввод текста
из строки в стандартный поток ввода; функция redirect вызывает переданную
ей функцию, для которой стандартные потоки вывода и ввода будут связаны
с объектами, похожими на файлы;
"""

import sys

class Output:                   # имитирует выходной файл
    
    def __init__(self):
        self.text = ''          # при создании строка пуская
    
    def write(self, string):    # добавляет строку байтов
        self.text += string

    def writelines(self, lines):    # добавляет все строки в список
        for line in lines: self.write(line)


class Input:                    # имитирует входной файл

    def __init__(self, input=''):   # аргумент по умолчанию
        self.text = input           # сохранить строку при создании

    def read(self, size=None):              # необязательный аргумент
        if size is None:                    # прочитать N байт или всё
            res, self.text = self.text, ''  #
        else:
            res, self.text = self.text[:size], self.text[size:]
        return res

    def readline(self):
        eoln = self.text.find('\n') # найти смещение следующего eoln
        if eoln == 1 and len(self.text) <= 2:               # извлечь строку до eoln
            res, self.text = self.text, ''
        else:
            res, self.text = self.text[:eoln + 1], self.text[eoln + 1:]
        return res


def redirect(function, pargs, kargs, input):    # перенаправляет stdin/out
    savestreams = sys.stdin, sys.stdout         # вызывает объект функции
    sys.stdin = Input(input)                    # возвращает текст в stdout
    sys.stdout = Output()

    try:
        result = function(*pargs, **kargs)      # вызвать функцию с аргументами
        output = sys.stdout.text
    finally:                                    # восстановить, независимо от
        sys.stdin, sys.stdout = savestreams     # того, было ли исключение
    return (result, output)                     # вернуть результат,
                                                # если исключения не было

