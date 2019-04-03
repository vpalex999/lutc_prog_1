"""
графический интерфейс, отображающий данные, производимые рабочими потоками
на основе классов
"""

import threading, queue, time
from tkinter.scrolledtext import ScrolledText


class ThreadGui(ScrolledText):

    threadsPerClick = 4

    def __init__(self, parent=None):
        ScrolledText.__init__(self, parent)
        self.pack()
        self.dataQueue = queue.Queue()
        self.bind('<Button-1>', lambda event: self.makethreads(event))
        self.consumer()

    def producer(self, id):
        for i in range(5):
            time.sleep(0.1)
            print('put')
            self.dataQueue.put("[producer id={}, count={}]".format(id, i))

    def consumer(self):
        try:
            print('get')
            data = self.dataQueue.get(block=False)
        except queue.Empty:
            pass
        else:
            self.insert('end', "consumer got => {}\n".format(str(data)))
            self.see('end')
        self.after(100, lambda: self.consumer())

    def makethreads(self, event):
        for i in range(self.threadsPerClick):
            threading.Thread(target=self.producer, args=(i,)).start()


if __name__ == '__main__':
    """ главный поток: порождает группу рабочих потоков на каждый щелчок мыши """
    root = ThreadGui()
    root.pack()
    root.mainloop()
