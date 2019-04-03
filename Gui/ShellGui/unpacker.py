""" Заглушка сценария packer """
import sys


def unpack(ifile):
    for line in open(ifile):
        print(line)


if __name__ == '__main__':
    unpack(sys.argv[1])
