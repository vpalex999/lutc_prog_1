"""
Отыскивает наибольший файл с исходным программным кодом на языке Python
в единственном каталоге.
Поиск выполняется в каталоге стандартной биб­лиотеки Python для Windows, если
в аргументе командной строки не был указан какой-то другой каталог.
"""

import os, glob, sys
dirname = r'C:\Python31\Lib' if len(sys.argv) == 1 else sys.argv[1]
print(dirname)

allsizes= []
allpy = glob.glob(dirname + os.sep + '*.py')
print(dirname + os.sep + '*.py')

for filename in allpy:
    filesize = os.path.getsize(filename)
    allsizes.append((filesize, filename))

allsizes.sort()
print(allsizes[:2])
print(allsizes[-2:])
