#!/usr/bin/python3.8
# -*- coding: utf-8 -*-


snail_func = lambda n: n and n.pop(0) + snail_func([list(array) for array in zip(*n)][::-1])

if __name__ == '__main__':
    user_array = [[1, 2, 3, 1], [4, 5, 6, 4], [7, 8, 9, 7], [7, 8, 9, 7]]
    for row in user_array:
        print(row)

    print(snail_func(user_array))
