import os, time

def child(pipeout):
    zzz = 0
    while True:
        time.sleep(zzz) # заставить родителя подождать
        msg = (f"Spam {zzz}").encode() # каналы - двоичные файлы
        os.write(pipeout, msg)  # отправить данные родителю
        zzz = (zzz+1) % 5 # переход к 0 после 4


def parent():
    pipein, pipeout = os.pipe()   # создать канал с 2 концами
    if os.fork() == 0:            # создатькопию процесса           
        child(pipeout)          # в копии вызвать child
    else:                       # в родителе слушать канал
        while True:
            line = os.read(pipein, 32)  # остановиться до получения данных
            print(f"Parent {os.getpid()} got [{line}] at {time.time()}")

parent()
