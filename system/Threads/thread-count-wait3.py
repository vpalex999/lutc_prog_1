"""
объект мьютекса, совместно используемый всеми потоками выполнения, передается
функции в виде аргумента; для автоматического приобретения/освобождения
блокировки используется менеджер контекста; чтобы избежать излишней нагрузки
в цикле ожидания, и для имитации выполнения продолжительных операций добавлен
вызов функции sleep
"""

import _thread as thread, time

stdoutmutex = thread.allocate_lock()
numthreads = 5
exitmutexes = [thread.allocate_lock() for i in range(numthreads)]


def counter(myId, count, mutex):    # мьютекс передаётся в аргументе
    for i in range(count):
        time.sleep(1 / (myId + 1))  #  различные доли секунды
        with mutex:                 # приобретает/освобождает поток
            print(f"[{myId}] => {i}")
    exitmutexes[myId].acquire()    # глобальные список/сигнал главному потоку


for i in range(numthreads):
    thread.start_new_thread(counter, (i, 5, stdoutmutex))

while not all(mutex.locked() for mutex in exitmutexes): time.sleep(0.25) # задержка основного потока увеличивает
print('Main thread exiting.')               # скорость обработки тредов

