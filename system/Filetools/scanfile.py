
def scanner(name, function):
    file = open(name, 'r')      # создать объект файла
    while True:
        line = file.readline()  # вызов метода файла
        if not line: break      # до конца файла
        function(line)          # вызвать объект функции
    file.close()


def scanner2(name, function):
    for line in open(name, 'r'):
        function(line)


def scanner3(name, function):
    list(map(function, open(name, 'r')))


def scanner4(name, function):
    [function(line) for line in open(name, 'r')]


def scanner5(name, function):
    list(function(line) for line in open(name, 'r'))
