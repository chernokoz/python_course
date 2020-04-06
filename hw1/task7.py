#!/usr/bin/env python3

# UNCOMMENT THIS FILE WHEN PROBLEM IS SOLVED


def verbing(word):
    if len(word) < 3:
        return word
    if word[-3:] == 'ing':
        ans = word[:-3] + 'ly'
    else:
        ans = word + 'ing'
    return ans


def not_bad(text):
    not_pointer = text.find('not')
    bad_pointer = text.find('bad')
    if not_pointer < bad_pointer:
        text = text[:not_pointer] + "good" + text[(bad_pointer + 3):]
    return text
