#!/usr/bin/env python3

from collections import namedtuple

Nil = namedtuple('Nil', ())
Cons = namedtuple('Cons', ('car', 'cdr'))


def null(lst):
    return lst == Nil()


def fromseq(seq):
    if seq:
        return Cons(seq[0], fromseq(seq[1:]))
    return Nil()


def head(lst):
    return lst.car


def tail(lst):
    return lst.cdr


def foldr(func, acc, lst):
    if null(lst):
        return acc
    return func(head(lst), foldr(func, acc, tail(lst)))


def foldl(func, acc, lst):
    if null(lst):
        return acc
    return foldl(func, func(acc, head(lst)), tail(lst))


def length(lst):
    return foldl(lambda len, _: len + 1, 0, lst)


def tolist(lst):
    return foldl(lambda x, y: (x.append(y), x)[1], [], lst)


def map_(func, lst):
    return foldr(lambda x, y: Cons(func(x), y), Nil(), lst)


def append(lst1, lst2):
    return foldr(Cons, lst2, lst1)


def filter_(pred, lst):
    return foldr(lambda x, y: Cons(x, y) if pred(x) else y, Nil(), lst)


def reverse(lst):
    return foldl(lambda x, y: Cons(y, x), Nil(), lst)


def elem(value, lst):
    return not null(filter_(lambda x: x == value, lst))
