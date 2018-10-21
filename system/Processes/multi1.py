"""
основы применения пакета multiprocessing: класс Process по своему действию
напоминает класс threading.Thread, но выполняет функцию в отдельном процессе,
а не в потоке; для синхронизации можно использовать блокировки, например, для
вывода текста; запускает новый процесс интерпретатора в Windows, порождает
дочерний процесс в Unix;
"""

import os
from multiprocessing import Process
from multiprocessing import Lock

def whoami(label, lock):
    msg = '{}: name:{}, pid:{}'.format(label, __name__, os.getpid())
    with lock:
        print(msg)

if __name__ == '__main__':
    lock = Lock()
    whoami('function call', lock)

    p = Process(target=whoami, args=('spawned child', lock))
    p.start()
    p.join()


    for i in range(5):
        Process(target=whoami, args=(('run process {}'.format(i)), lock)).start()

    with lock:
        print('Main process exit.')



