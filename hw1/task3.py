#!/usr/bin/env python3

# UNCOMMENT THIS FILE WHEN PROBLEM IS SOLVED

import sys


def nl_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
    for i in enumerate(lines):
        print(i[0] + 1, i[1], sep='\t')


def nl_from_stdin():
    num = 1
    while True:
        try:
            line = input()
        except EOFError:
            return
        print(num, line, sep='\t')
        num += 1


def main(args):
    """this function is an entry point, should handle sys.argv properly
    and call appropriate function

    see tests/test_task3.py for test examples
    """

    if len(args) == 0:
        nl_from_stdin()
    elif len(args) == 1:
        nl_from_file(args[0])
    else:
        raise ValueError("Error! Too many arguments!")

if __name__ == '__main__':
    main(sys.argv)
