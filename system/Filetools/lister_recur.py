""" выводит список файлов в дереве каталогов с применением рекурсии """

import sys, os

def mylister(currdir):
    print('[' + currdir + ']')
    for file in os.listdir(currdir):        # генерирует список файлов
        path = os.path.join(currdir, file)  # добавить путь к каталогу
        if not os.path.isdir(path):
            print(path)
        else:
            mylister(path)  # рекурсивный спуск в подкаталоги


if __name__ == '__main__':
    mylister(sys.argv[1]) # имя каталога в командной строке