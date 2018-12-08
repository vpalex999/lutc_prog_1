"""
##############################################################################
Пытается проигрывать медиафайлы различных типов. Позволяет определять
специализированные программы-проигрыватели вместо использования универсального
приема открытия файла в веб-броузере. В текущем своем виде может не работать
в вашей системе; для открытия аудиофайлов в Unix используются фильтры и команды,
в Windows используется команда start, учитывающая ассоциации с расширениями
имен файлов (то есть для открытия файлов .au, например, она может запустить
проигрыватель аудиофайлов или веб-броузер). Настраивайте и расширяйте сценарий
под свои потребности. Функция playknownfile предполагает, что вы знаете, какой
тип медиафайла пытаетесь открыть, а функция playfile пробует определить тип
файла автоматически, используя модуль mimetypes; обе они пробуют запустить веб-
броузер с помощью модуля webbrowser, если тип файла не удается определить.
##############################################################################
"""

import os, sys, mimetypes, webbrowser

helpmsg = """
Sorry: can’t find a media player for ‘{}’ on your system!
Add an entry for your system to the media player dictionary
for this type of file in playfile.py, or play the file manually.
"""

def trace(*args): print(*args)

##############################################################################
# приемы проигрывания: универсальный и другие: дополните своими приемами
##############################################################################


class MediaTool(object):
    def __init__(self, runtext=''):
        self.runtext = runtext

    def run(self, mediafile, **options):
        fullpath = os.path.abspath(mediafile)
        self.open(fullpath, **options)


class Filter(MediaTool):
    def open(self, mediafile, **ignored):
        media = open(mediafile, 'rb')
        player = os.popen(self.runtext, 'w')
        player.write(media.read())


class Cmdline(MediaTool):
    def open(self, mediafile, **ignored):
        cmdline = self.runtext.format(mediafile)
        os.system(cmdline)


class Winstart(MediaTool):
    def open(self, mediafile, wait=False, **other):
        if not wait:
            os.startfile(mediafile)
        else:
            os.system('start /WAIT' + mediafile)


class Webbrowser(MediaTool):
    def open(self, mediafile, **options):
        webbrowser.open_new('file://{}'.format(mediafile), **options)


##############################################################################
# медиа- и платформозависимые методы: измените или укажите один из имеющихся
##############################################################################

# соответствия платформ и проигрывателей: измените!

audiotools = {
    'sunos5': Filter('/usr/bin/audioplay'),   # os.popen().write()
    'linux2': Cmdline('cat {} > /dev/audio'),
    'sunos4': Filter('/usr/demo/SOUND/play'),
    'win32': Winstart(),
    #'win32': Cmdline('start {}')
}


videotools = {
    'linux2': Cmdline('tkcVideo_c700 {}'),
    'win32': Winstart(),
}


imagetools = {
    'linus2': Cmdline('vi {}'),
    'win32': Cmdline('notepad {}'),
}


texttools = {
    'linux2': Cmdline('vi {}'),
    'win32': Cmdline('notepad {}'),
}


apptools = {
    'win32': Winstart()
}


# таблица соответствия между типами файлов и программами-проигрывателями
mimetable = {
             'audio': audiotools,
             'video': videotools,
             'image': imagetools,
             'text': texttools,
             'application': apptools
             }

# не-html текст: броузер
##############################################################################
# интерфейсы высокого уровня
##############################################################################


def trywebbrowser(filename, helpmsg=helpmsg, **options):
    """
    пытается открыть файл в как последнее средство,
    а также для файлов типа helpmsg=helpmsg, **options):
    веб-броузере если тип файла или платформы неизвестен, text/html
    """
    trace('trying browser', filename)
    try:
        player = Webbrowser()
        player.run(filename, **options)
    except:
        print(helpmsg.format(filename))


def playknownfile(filename, playertable={}, **options):
    """
    проигрывает медиафайл известного типа: использует программы-проигрыватели
    для данной платформы или запускает веб-броузер, если для этой платформы не
    определено ничего другого; принимает таблицу соответствий расширений и
    программ-проигрывателей
    """
    if sys.platform in playertable:
        playertable[sys.platform].run(filename, **options)
    else:
        trywebbrowser(filename, **options)


def playfile(filename, mimetable=mimetable, **options):
    """
    проигрывает медиафайл любого типа: использует модуль mimetypes для
    пределения типа медиафайла и таблицу соответствий между расширениями и
    рограммами-проигрывателями; запускает веб-броузер для файлов с типом
    ext/html, с неизвестным типом и при отсутствии таблицы соответствий
    """
    contenttype, encoding = mimetypes.guess_type(filename)
    if contenttype is None or encoding is not None:
        contenttype = '?/?'
    maintype, subtype = contenttype.split('/', 1)
    if maintype == 'text' and subtype == 'html':
        trywebbrowser(filename, **options)
    elif maintype in mimetable:
        playknownfile(filename, mimetable[maintype], **options)
    else:
        trywebbrowser(filename, **options)


##############################################################################
# программный код самопроверки
##############################################################################

if __name__ == '__main__':
    playfile('system/Media/playfile.py')

