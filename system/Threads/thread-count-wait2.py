"""
использование простых глобальных данных (не мьютексов) для определения момента
завершения всех потоков в родительском/главном потоке; потоки совместно
используют список, но не его элементы, при этом предполагается, что после
создания список не будет перемещаться в памяти
"""

import _thread as thread, time

stdoutmutex = thread.allocate_lock()
exitmutexes = [False] * 10


def counter(myId, count):
    for i in range(count):
        stdoutmutex.acquire()
        print(f"[{myId}] => {i}")
        stdoutmutex.release()
    exitmutexes[myId] = True    # сигнал главному потоку


for i in range(10):
    thread.start_new_thread(counter, (i, 100))

while False in exitmutexes: time.sleep(0.1) # задержка основного потока увеличивает
print('Main thread exiting.')               # скорость обработки тредов

