"""
использование мьютексов в родительском/главном потоке выполнения для определения
момента завершения дочерних потоков, взамен time.sleep; блокирует stdout, чтобы
избежать конфликтов при выводе;
"""

import _thread as thread

stdoutmutex = thread.allocate_lock()
exitmutexes = [thread.allocate_lock() for i in range(10)]


def counter(myId, count):
    for i in range(count):
        stdoutmutex.acquire()
        print(f"[{myId}] => {i}")
        stdoutmutex.release()
    exitmutexes[myId].acquire()


for i in range(10):
    thread.start_new_thread(counter, (i, 100))

for mutex in exitmutexes:
    while not mutex.locked(): pass
print('Main thread exiting.')

