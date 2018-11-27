"""
отыскивает и удаляет все файлы “*.pyc” с байт-кодом в дереве каталогов, имя
которого передается в виде аргумента командной строки; предполагает наличие
непереносимой Unix-подобной команды find
"""

import os, sys

rundir = sys.argv[1]

if sys.platform[:3] == 'win':
    findcmd = r'c:\cygwin\bin\find %s -name "*.pyc" -print' % rundir
else:
    findcmd = 'find {} -name "*.pyc" -print'.format(rundir)

print(findcmd)

count = 0
for filename in os.popen(findcmd):
    count += 1
    print(filename, end='')
    os.remove(filename.rstrip())

print('Removed {} .pyc files'.format(count))