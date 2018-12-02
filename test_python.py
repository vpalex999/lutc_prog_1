msg = 'Hello World!'
print(msg)
msg2 = "Hello Oleg!"
print(msg2)


class Dn(object):
    def __init__(self, number):
        self.number = number


def test_sorted():
    dn1 = Dn('3436873639')
    dn2 = Dn('3436842446')

    list_dn = [dn1, dn2]

    sort_dn = sorted(list_dn, key=lambda x: int(x.number))

    assert sort_dn[0].number == '3436842446'
