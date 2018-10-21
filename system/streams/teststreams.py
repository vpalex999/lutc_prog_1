""" читает числа до символа конца файла и выводит их квадраты """

def interact():
    print('Hello stream world') # print выводит в sys.stdout

    while True:
        try:
            reply = input('Enter a number>')    # input читает из sys.stdin
        except EOFError:
            break   # исключение при всрече символа eof
        else:       # входные данные в виде строки
            num = int(reply)
            print(f"{num} squared is {num ** 2}")
    print('Bye')


if __name__ == '__main__':
    interact()  # если выполняется, а не импортируется