"""
##############################################################################
реализует два набора инструментов, специфичных для типов
##############################################################################
"""

from shellgui import *
from packdlg import runPackDialog
#from unpkdlg import runUnpackDialog

runUnpackDialog = ""


class TextPack1(ListMenuGui):
    def __init__(self):
        self.myMenu = [
            ('Pack  ', runPackDialog),
            ('Unpack', runUnpackDialog),
            ('Mtool ', self.notdone)
        ]

        ListMenuGui.__init__(self)

    def forToolBar(self, label):
        return label in {'Pack  ', 'Unpack'}


class TextPack2(DictMenuGui):
    def __init__(self):
        self.myMenu = {'Pack  ': runPackDialog,
                       'Unpack': runUnpackDialog,
                       'Mtool ': self.notdone}

        DictMenuGui.__init__(self)


if __name__ == '__main__':
    from sys import argv

    if len(argv) > 1 and argv[1] == 'list':
        print('list test')
        TextPack1().mainloop()
    else:
        print('dict test')
        TextPack2().mainloop()
