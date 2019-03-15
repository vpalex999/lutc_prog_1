"""
Общесистемные утилиты поддержки многопоточной модели выполнения для графических интерфейсов.

Реализует единую очередь обработчиков и цикл обработки событий от таймера для
ее проверки, совместно используемые всеми окнами в программе; рабочие потоки
помещают в очередь свои обработчики завершения и протекания операции для вызова
в главном потоке; эта модель не блокирует графический интерфейс – он просто
выполняет операции в порождаемых дочерних потоках и обрабатывает события
завершения и продолжения операций; рабочие потоки могут перекрываться во
времени с главным потоком и с другими рабочими потоками.

На практике передача функций-обработчиков с аргументами через очереди намного
удобнее, чем передача простых данных, если в программе одновременно могут
действовать разнотипные потоки выполнения, – каждый тип может подразумевать
выполнение различных действий при завершении.

Библиотеки создания графических интерфейсов не полностью поддерживают
многопоточную модель, поэтому, вместо того чтобы напрямую вызывать обработчики,
производящие изменение графического интерфейса после выполнения основной
операции в потоке, они помещаются в общую очередь и вызываются не в дочерних
потоках, а в цикле обработки событий от таймера в главном потоке; это также
обеспечивает регулярность и предсказуемость моментов обновления графического
интерфейса; требуется, чтобы логика потока разбивалась на основную операцию,
завершающие действия и операцию, возвращающую информацию о протекании процесса.

Предполагается, что в случае неудачи функция потока возбуждает исключение
и принимает в аргументе ‘progress’ функцию обратного вызова, если поддерживает
возможность передачи информации о ходе выполнения операции; предполагается
также, что все обработчики выполняются очень быстро, либо производят обновление
графического интерфейса в процессе работы, и эта очередь будет содержать функции
обратного вызова (или другие вызываемые объекты) для использования в приложениях
с графическим интерфейсом, – требуется наличие виджетов, чтобы обеспечить работу
цикла на основе метода ‘after’; для использования данной модели в сценариях без
графического интерфейса можно было бы использовать простой таймер.
"""

# запустить, даже если нет потоков # сейчас, если модуль threads
try:
    import _thread as thread
except ImportError:
    import _dummy_thread as thread

# общая очередь
# в глобальной области видимости, совместно используется потоками
import queue
import sys

threadQueue = queue.Queue(maxsize=0)  # infinite size

##############################################################################
# ГЛАВНЫЙ ПОТОК – периодически проверяет очередь; выполняет действия,
# помещаемые в очередь, в контексте главного потока; один потребитель (GUI) и
# множество производителей (загрузка, удаление, отправка); простого списка
# было бы вполне достаточно, если бы операции list.append и list.pop были
# атомарными; 4 издание: в процессе обработки каждого события от таймера
# выполняет до N операций: обход в цикле всех обработчиков, помещенных в
# очередь, может заблокировать графический интерфейс, а при выполнении
# единственной операции вызов всех обработчиков может занять продолжительное
# время или привести к неэффективному расходованию ресурсов процессора на
# обработку событий от таймера (например, информирование о ходе выполнения
# операций); предполагается, что обработчики выполняются очень быстро или
# выполняют обновление графического интерфейса в процессе работы (вызывают
# метод update): после вызова обработчика планируется очередное событие от
# таймера и управление возвращается в цикл событий; поскольку этот цикл
# выполняется в главном потоке, он не препятствует завершению программы;
##############################################################################


def threadChecker(widget, delayMsecs=100, perEvent=1):
    for i in range(perEvent):
        try:
            (callback, args) = threadQueue.get(block=False)
        except queue.Empty:
            break
        else:
            callback(*args)

    widget.after(delayMsecs, lambda: threadChecker(widget, delayMsecs, perEvent))


##############################################################################
# НОВЫЙ ПОТОК – выполняет задание, помещает в очередь обработчик завершения и
# обработчик, возвращающий информацию о протекании процесса; вызывает функцию
# основной операции с аргументами, затем планирует вызов функций on* с
# контекстом; запланированные вызовы добавляются в очередь и выполняются в
# главном потоке, чтобы избежать параллельного обновления графического
# интерфейса; позволяет программировать основные операции вообще без учета
# того, что они будут выполняться в потоках; не вызывайте обработчики в
# потоках: они могут обновлять графический интерфейс в потоке, поскольку
# передаваемая функция будет вызвана в потоке; обработчик ‘progress’ просто
# должен добавлять в очередь функцию обратного вызова с передаваемыми ей
# аргументами; не обновляйте текущие счетчики здесь: обработчик завершения
# будет извлечен из очереди и выполнен функцией threadChecker в главном
# потоке;
##############################################################################


def threaded(action, args, context, onExit, onFail, onProgress):
    try:
        if not onProgress:  #
            action(*args)
        else:
            def progress(*any):
                threadQueue.put((onProgress, any + context))
            action(progress=progress, *args)
    except Exception:
        threadQueue.put((onFail, (sys.exc_info(), ) + context))
    else:
        threadQueue.put((onExit, context))


def startThread(action, args, context, onExit, onFail, onProgress=None):
    thread.start_new_thread(threaded, (action, args, context, onExit, onFail, onProgress))


##############################################################################
# счетчик или флаг с поддержкой многопоточной модели выполнения: удобно
# использовать, чтобы избежать выполнения перекрывающихся во времени операций,
# когда потоки изменяют другие общие данные, помимо тех, которые изменяются
# обработчиками, помещаемыми в очередь
##############################################################################

class ThreadCounter:
    def __init__(self):
        self.count = 0
        self.mutex = thread.allocate_lock()

    def incr(self):
        self.mutex.acquire()
        self.count += 1
        self.mutex.release()

    def decr(self):
        self.mutex.acquire()
        self.count -= 1
        self.mutex.release()

    def __len__(self):
        return self.count

##############################################################################
# реализация самотестирования: разбивает поток на основную операцию,
# операцию завершения и операцию информирования о ходе выполнения задания
##############################################################################


if __name__ == '__main__':
    import time
    from tkinter.scrolledtext import ScrolledText

    def onEvent(i):
        myname = 'thread-{}'.format(i)
        startThread(
            action=threadaction,
            args=(i, 3),
            context=(myname,),
            onExit=threadexit,
            onFail=threadfail,
            onProgress=threadprogress
        )

    # основная операция, выполняемая потоком
    def threadaction(id, resp, progress):
        for i in range(resp):
            time.sleep(1)
            if progress:
                progress(i)
        if id % 2 == 1:
            raise Exception

    # обработчики завершения/информирования о ходе выполнения задания:
    # передаются главному потоку через очередь
    def threadexit(myname):
        text.insert('end', '{}\texit\n'.format(myname))
        text.see('end')

    def threadfail(exc_info, myname):
        text.insert('end', '{}\tfail\t{}\n'.format(myname, exc_info[0]))
        text.see('end')

    def threadprogress(count, myname):
        text.insert('end', '{}\tprog\t{}\n'.format(myname, count))
        text.see('end')
        text.update()

    # создать графический интерфейс и запустить цикл обработки событий от
    # таймера в главном потоке
    # порождать группу рабочих потоков в ответ на каждый щелчок мышью:
    # выполнение их может перекрываться во времени

    text = ScrolledText()
    text.pack()
    threadChecker(text)
    text.bind('<Button-1>', lambda event: list(map(onEvent, range(6))))

    text.mainloop()
