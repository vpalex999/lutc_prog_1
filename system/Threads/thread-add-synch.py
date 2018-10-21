"""
всегда выводит 200 - благодаря синхронизации доступа к глобальному ресурсу
"""

import threading, time

count = 0

addlock = threading.Lock()

def adder():
    global count
    with addlock:
        count = count + 1
    time.sleep(0.5)
    with addlock:
        count = count + 1


threads = []

for i in range(100):
    thread = threading.Thread(target=adder, args=())
    thread.start()
    threads.append(thread)


for thread in threads: thread.join()
print(count)
