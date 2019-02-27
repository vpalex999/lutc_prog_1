"""
графический интерфейс, отображающий данные, производимые рабочими потоками
"""

import _thread, queue, time

dataQueue = queue.Queue()


def producer(id):
    for i in range(5):
        time.sleep(0.1)
        print('put')
        dataQueue.put("[producer id={}, count={}]".format(id, i))


def consumer(root):
    try:
        print('get')
        data = dataQueue.get(block=False)
    except queue.Empty:
        pass
    else:
        root.insert('end', "consumer got => {}\n".format(str(data)))
        root.see('end')
    root.after(250, lambda: consumer(root))


def makethreads():
    for i in range(4):
        _thread.start_new_thread(producer, (i,))


if __name__ == '__main__':
    """ главный поток: порождает группу рабочих потоков на каждый щелчок мыши """
    from tkinter.scrolledtext import ScrolledText
    root = ScrolledText()
    root.pack()
    root.bind('<Button-1>', lambda event: makethreads())
    consumer(root)
    root.mainloop()
