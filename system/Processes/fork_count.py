"""
Основы ветвления: запустить 5 копий этой программы параллельно оригиналу; каждая
копия считает до 5 и выводит счетчик в тот же поток stdout -- при ветвлении
копируется память процесса, в том числе дескрипторы файлов; в настоящее время
ветвление не действует в Windows без Cygwin: запускайте программы в Windows
с помощью функции os.spawnv или пакета multiprocessing; функция spawnv примерно
соответствует комбинации функций fork+exec;
"""

import os, time

def counter(count): # вызывается в новом процессе
    for i in range(count):
        time.sleep(1)
        print(f"[{os.getpid()}] => i")


for i in range(5):
    pid = os.fork()
    if pid != 0:                        # в родительском процессе:
        print(f"Process {pid} spawned") # продолжить цикл
    else:
        counter(5)  # в дочернем процессе
        os._exit(0) # вызвать функцию и завершиться

print('Main process exiting.')  # родитель не должен ждать