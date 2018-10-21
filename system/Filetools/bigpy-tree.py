"""
Отыскивает наибольший файл с исходным программным кодом на языке Python в дереве
каталогов.
Поиск выполняется в каталоге стандартной биб­лиотеки, отображение результатов
выполняется с помощью модуля pprint.
"""


import sys, os, pprint

trace = False

if sys.platform.startswith('win'):
    dirname = r'C:Python31\Lib' if len(sys.argv) == 1 else sys.argv[1]
else:
    dirname = '/usr/bin/python'

dirname = dirname if len(sys.argv) == 1 else sys.argv[1]

allsizes = []

for (thisDir, subHere, filesHere) in os.walk(dirname):
    if trace: print(thisDir)
    for filename in filesHere:
        if filename.endswith('.py'):
            if trace: print('...', filename)
            fullname = os.path.join(thisDir, filename)
            fullsize = os.path.getsize(fullname)
            allsizes.append((fullsize, filename))

allsizes.sort()
pprint.pprint(allsizes[:2])
pprint.pprint(allsizes[-2:])