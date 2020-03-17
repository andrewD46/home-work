#!/usr/bin/python3.8
# -*- coding: utf-8 -*-


def extra(array):
    for i in range(len(array)):
        f = True
        for j in range(len(array)):
            if array[i] == array[j] and i != j:
                f = False
                break
        if f:
            return array[i]


if __name__ == "__main__":
    user_array = list(map(int, input('Введите значения через пробел: ').split()))
    print(extra(user_array))
