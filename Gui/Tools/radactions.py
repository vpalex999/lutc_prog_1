# обработчики: перезагружаются перед каждым вызовом


def message1():
    print('spamSpamSPAM')


def message2(self):
    print('Ni! Ni!2')
    self.method1()
