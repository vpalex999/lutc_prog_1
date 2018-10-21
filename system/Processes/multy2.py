"""
Реализует взаимодействие с помощью анонимных каналов из пакета multiprocessing.
Возвращаемые 2 объекта Connection представляют концы канала: объекты передаются
в один конец и принимаются из другого конца, хотя каналы по умолчанию являются
двунаправленными
"""

import os
from multiprocessing import Process, Pipe

def sender(pipe):
    """
    передает объект родителю через анонимный канал
    """
    pipe.send(['spam']+[42, 'eggs'])
    pipe.close()

def talker(pipe):
    """
    передает и принимает объекты из канала
    """
    pipe.send(dict(name='Bob', spam=42))
    reply = pipe.recv()
    print('talker got: ', reply)


if __name__ == '__main__':
    (parentEnd, childEnd) = Pipe()
    Process(target=sender, args=(childEnd,)).start()   # породить потомка
                                                        # с каналом
    print('parent got: ', parentEnd.recv()) # принять от потомка
    parentEnd.close()                       # или может быть закрыт
                                            # автоматически сборщиком
                                            # мусора
    (parentEnd, childEnd) = Pipe()
    child = Process(target=talker, args=(childEnd,))
    child.start()

    print('parent got: ', parentEnd.recv()) # принять от потомка
    parentEnd.send({x*2 for x in 'spam'})   # передать потомку
    child.join()    # ждать завершения потомка
    print('parent exit.')
