#!/usr/bin/python3.8
# -*- coding: utf-8 -*-

from collections.abc import Sequence


def flatten(lst):
    for el in lst:
        if isinstance(el, Sequence) and not isinstance(el, str):
            yield from flatten(el)
        else:
            yield el


if __name__ == '__main__':
    print(list(flatten([1, 2, [3, 4, [5, 6], 7], [8, [9, [10]]]])))
    print(list(flatten([1, [2, 3, [4, 5], 6, 7], 8, 9, 10])))
    print(list(flatten([1, 2, 3])))
    print(list(flatten([])))
