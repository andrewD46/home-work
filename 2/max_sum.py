#!/usr/bin/python3.8
# -*- coding: utf-8 -*-


def max_sum(array):
    d = dict((array.index(i) + 1, i) for i in array)
    return d


if __name__ == '__main__':
    print(max_sum([-2, 1, 3, -4, 5]))
