

def foo():
    x = 4
    def bar():
        print(x)
    bar()
    x = 5
    bar()
    return bar

x = 'aaa'
f = foo()
print(x)
f()