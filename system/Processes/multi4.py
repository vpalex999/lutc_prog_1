"""
От класса Process можно породить подкласс, так же, как от класса threading.
Thread;
объект Queue действует подобно queue.Queue, но обеспечивает обмен данными между
процессами, а не между потоками выполнения
"""

import os, time, queue
from multiprocessing import Process, Queue  # общая очередь для процессов
                                            # очередь - это канал +
                                            # блокировки/семафоры


class Counter(Process):
    label = ' @'
    def __init__(self, start, queue):    # сохраняет данные для
        self.state = start              # использования в методе run
        self.post = queue
        Process.__init__(self)

    def run(self):          # вызывается в новом процессе
        for i in range(3):  # метод start()
            time.sleep(1)
            self.state += 1
            print(self.label, self.pid, self.state) # self.pid - pid потока
            self.post.put([self.pid, self.state])   # stdout совместно используется всеми
        print(self.label, self.pid, '-')

if __name__ == '__main__':
    print('start', os.getpid())
    expected = 9

    post = Queue()
    p = Counter(0, post)    # запустить три процесса, использующих общую очередь
    q = Counter(100, post)  # потомки являются производителями
    r = Counter(1000, post)
    p.start(); q.start(); r.start()

    while expected:     # родитель потребляет данные из очереди
        time.sleep(0.5) # очень напоминиет графический интерфейс,
        try:
            data = post.get(block=False)
        except queue.Empty:
            print('no data...')
        else:
            print('posted:', data)
            expected -= 1

    p.join(); q.join(); r.join()    # дождаться завершения дочерних процессов
    print('finish', os.getpid(), r.exitcode)    # exitcode - код завершения потока