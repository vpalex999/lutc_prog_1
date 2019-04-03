""" Заглушка сценария packer """
import sys, glob


def pack(ofile, ifiles):
    output =open(ofile, 'w')
    for name in ifiles:
        print('packing:', name)
        output.write(name + '\n')


if __name__ == '__main__':
    ifiles = []
    for patt in sys.argv[2:]:
        print(glob.glob(patt))
        ifiles += glob.glob(patt)
    pack(sys.argv[1], ifiles)
