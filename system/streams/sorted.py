import sys

lines = sys.stdin.readlines()           # читает входные строки из stdin
lines.sort()                            # сортирует их
for line in lines: print(line, end='')  # отправляет результаты в stdout
                                        # для дальнейшей обработки
                                        