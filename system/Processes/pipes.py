"""
запускает дочерний процесс/программу, соединяет свои потоки stdin/stdout
с потоками stdout/stdin дочернего процесса -- операции чтения и записи на
стороне родительского процесса отображаются на стандартные потоки ввода-вывода
дочерней программы; напоминает соединение потоков с помощью модуля subprocess;
"""

import os, sys

def spawn(prog, *args): # имя программы, фргументы командной строки
    stdinFd = sys.stdin.fileno()    # получить дискрипторы потоков
    stdoutFd = sys.stdout.fileno()  # обычно stdin=0, stdout=1

    parentStdin, childStdout = os.pipe()    # создать два канала IPC
    childStdin, parentStdout = os.pipe()    # 
    pid = os.fork() # создать копию процесса
    if pid:
        os.close(childStdout)       # в родительском после ветвления
        os.close(childStdin)        # закрыть дочерние процессы в родителе
        os.dup2(parentStdin, stdinFd)   # копия sys.stdin = pipe1[0]
        os.dup2(parentStdout, stdoutFd) # копия sys.stdout = pipe2[1]
    else:
        os.close(parentStdin)           # в дочернем после ветвления
        os.close(parentStdout)          # закрыть родительские концы
        os.dup2(childStdin, stdinFd)    # копия sys.stin = pipe2[0]
        os.dup2(childStdout, stdoutFd)  # копия sys.stdout = pipe1[1]
        args = (prog,) + args
        os.execvp(prog, args)   # запустить новую программу
        assert False, 'execvp failed!'  # os.exec никогда не вернётся сюда


if __name__ == '__main__':
    mypid = os.getpid()
    spawn('python', '-u', 'pipes-testchild.py', 'spam')   # породить дочернюю прог.

    print('Hello 1 from parent ', mypid)    # в stdin дочерней прогр.
    #sys.stdout.flush()                      # вытолкнуть буфер stdio
    reply = input() # из потока ввода потомка
    sys.stderr.write(f"Parent got: {reply}\n") # stderr не связан с каналом

    print('Hello 2 from parent ', mypid)
    #sys.stdout.flush()
    reply = sys.stdin.readline()
    sys.stderr.write(f"Parent got: {reply[:1]}")