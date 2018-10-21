""" функция os._exit() неуязвима для инструкций обработки исключений """


def outhere():
    import os
    print('Bye os world')
    os._exit(99)
    print('Never reached')

if __name__ == '__main__': outhere()
