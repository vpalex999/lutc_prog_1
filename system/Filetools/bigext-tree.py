"""
Отыскивает наибольший файл заданного типа в произвольном дереве каталогов.
Пропускает каталоги, которые уже были просканированы; перехватывает ошибки;
добавляет возможность вывода трассировки поиска и подсчета строк.
Кроме того, использует множества, итераторы файлов и генераторы, чтобы избежать
загрузки содержимого файлов целиком, и пытается обойти проблемы, возникающие при
выводе недекодируемых имен файлов/каталогов.
"""

import os, pprint
from sys import argv, exc_info

trace = 1       # 0=выкл, 1=каталоги, 2=+файлы
dirname, extname = os.curdir, '.py' # по умолчанию файлы .py в cwd

if len(argv) > 1: dirname = argv[1]     # например: C:\, C:\Python31\Lib
if len(argv) > 2: extname = argv[2]     # например: .pyw, .txt
if len(argv) > 3: trace = int(argv[3])  # например: ". .py 2"

def tryprint(arg):
    try:
        print(arg)  # непечатаемое имя файла?
    except UnicodeEncodeError:
        print(arg.encode()) # вывести как строку байтов

visited = set()
allsizes = []

for (thisDir, subsHere, filesHere) in os.walk(dirname):
    if trace: tryprint(thisDir)
    thisDir = os.path.normpath(thisDir)
    fixname = os.path.normcase(thisDir)
    if fixname in visited:
        if trace: tryprint('skipping' + thisDir)
    else:
        visited.add(fixname)
        for filename in filesHere:
            if filename.endswith(extname):
                if trace > 1: tryprint('+++' + filename)
                fullname = os.path.join(thisDir, filename)
                try:
                    bytesize = os.path.getsize(fullname)
                    linesize = sum(+1 for line in open(fullname, 'rb'))
                except Exception:
                    print('error', exc_info()[0])
                else:
                    allsizes.append((bytesize, linesize, fullname))


for (title, key) in [('bytes', 0), ('lines', 1)]:
    print('\nBy {}...'.format(title))
    allsizes.sort(key=lambda x: x[key])
    pprint.pprint(allsizes[:3])
    pprint.pprint(allsizes[-3:])
