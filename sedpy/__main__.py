import sys
import sedpy
from .sedpy import replace


def main():
    print('in main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))

    replace(sys.argv[1], sys.argv[2], sys.argv[3])


if __name__ == '__main__':
    main()