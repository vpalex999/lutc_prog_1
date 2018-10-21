"""
синхронизирует доступ к stdout: так как это общий глобальный объект, данные,
которые выводятся из потоков выполнения, могут перемешиваться, если не
синхронизировать операции
"""

import _thread as thread, time

mutex = thread.allocate_lock()  # создать объект блокировки

def counter(myId, count):   # эта функция выполняется в потоках

    for i in range(count):
        time.sleep(1)   #   имитировать работу
        mutex.acquire()             # теперь работа 
        print(f"[{myId}] => {i}")   # функции print
        mutex.release()             # не будет прерываться


for i in range(5):
    thread.start_new_thread(counter, (i, 5))    #

time.sleep(6)
print('Main thread exiting.')
