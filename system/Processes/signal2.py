# -*- coding: utf-8 -*-

"""
установка сигналов по истечении времени ожидания и их обработка на языке Python;
функция time.sleep некорректно ведет себя при появлении сигнала SIGALARM
(как и любого другого сигнала на моем компьютере, работающем под управлением
Linux), поэтому здесь вызывается функция signal.pause, которая приостанавливает
выполнение сценария до получения сигнала;
"""

import sys, signal, time

def now(): return time.ctime(time.time()) # строка с текущим временем

def onSignal(signum, stackframe):   # обработчик сигнала
    print('Got signal ', signum, ' at ', now()) # большинство обработчиков
                                                # остаются действующими

while True:
    print('Setting at ', now())
    signal.signal(signal.SIGALRM, onSignal) # установить обработчик сигнала
    signal.alarm(5)     # послать сигнал через 5 сек.
    signal.pause()      # ждать сигнал (или: pass) 
               