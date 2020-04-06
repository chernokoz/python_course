#!/usr/bin/env python3

# UNCOMMENT THIS FILE WHEN PROBLEM IS SOLVED

import sys


def tail_from_stdin():
    last_10_lines = []
    while True:
        try:
            line = input()
        except EOFError:
            for elem in last_10_lines:
                print(elem)
            return

        if len(last_10_lines) == 10:
            last_10_lines.pop(0)
            last_10_lines.append(line)
        else:
            last_10_lines.append(line)


def tail_from_file(filename):
    last_10_lines = []
    with open(filename) as file:
        for line in file:
            if len(last_10_lines) == 10:
                last_10_lines.pop(0)
                last_10_lines.append(line)
            else:
                last_10_lines.append(line)
    for elem in last_10_lines:
        print(elem, end='')


def tail_from_files(filenames):
    if len(filenames) > 1:
        for file in filenames:
            print('==>', file, '<==')
            tail_from_file(file)
    else:
        tail_from_file(filenames[0])


def main(args):
    """this function is an entry point, should handle sys.argv properly
    and call appropriate function

    see tests/test_task4.py for test examples
    """

    if len(args) == 1:
        tail_from_stdin()
    else:
        tail_from_files(args[1:])


if __name__ == '__main__':
    main(sys.argv)
