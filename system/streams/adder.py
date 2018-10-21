import sys

sum = 0

while True:
    try:
        line = input()      # или sys.stdin.readlines()
    except EOFError:        # или for line in sys.stdin:
        break               # input отсекает символы \n в конце строк
    else:
        sum += int(line)    #
print(sum)