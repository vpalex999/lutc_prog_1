import _thread


def action(i):      # простая функция
    print(i ** 32)


class Power:
    def __init__(self, i):
        self.i = i

    def action(self):       # связанный метод
        print(self.i ** 32)

    
_thread.start_new_thread(action, (2,))  # запуск простой функции

_thread.start_new_thread((lambda: action(2)), ())   # запуск lambda функции

obj = Power(2)
_thread.start_new_thread(obj.action, ())    # запуск связанного метода
