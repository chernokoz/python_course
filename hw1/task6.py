# #!/usr/bin/env python3
#
# # UNCOMMENT THIS FILE WHEN PROBLEM IS SOLVED
#
#
from collections import OrderedDict


def reverse_dictionary(dictionary):
    ans = {}
    for key, val in dictionary.items():
        for i in val:
            word = ans.get(i, [])
            word.append(key)
            ans[i] = word
    res = OrderedDict(sorted(ans.items()))
    return res


def parse_dictionary(text):
    elements = text.split('\n')
    elements.pop()
    ans = {}
    for elem in elements:
        word = elem.split(' - ')
        ans[word[0]] = word[1].split(', ')
    return ans


def print_dictionary(dictionary):
    for key, word in dictionary.items():
        print(key, ' - ', sep='', end='')
        for i in enumerate(word):
            print(i[1], end='')
            if i[0] != (len(word) - 1):
                print(', ', end='')
        print()


def main(text):
    base_dictionary = parse_dictionary(text)
    reversed_dictionary = reverse_dictionary(base_dictionary)
    print_dictionary(reversed_dictionary)
