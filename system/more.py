"""
разбивает строку или текстовый файл на страницы для интерактивного просмотра
"""

def more(text, numlines=15):
    lines = text.splitlines()   # подобно split('\n') но без '' в конце

    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk: print(line)
        if lines and input('More?') not in ['y', 'Y']: break

if __name__ == '__main__':
    import sys                          # если запускается как сценарий
    if len(sys.argv) == 1:              # вывести данные из stdin, если нет аргументов
        more(sys.stdin.read())
    else:
        more(open(sys.argv[1]).read(), 10)  # отобразить постранично содержимое
                                            # файла, указанного в командной строке