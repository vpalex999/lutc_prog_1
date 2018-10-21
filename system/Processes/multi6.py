"""
Плюс многое другое: пулы процессов, менеджеры, блокировки,
условные переменные,...
"""

import os
from multiprocessing import Pool


def powers(x):
    #print(os.getpid())
    return 2 ** x


if __name__ == '__main__':
    workers = Pool(processes=5)

    result = workers.map(powers, [2]*100)
    print(result[:16])
    print(result[-2:])

    results = workers.map(powers, range(100))
    print(results[:16])
    print(results[-2:])
