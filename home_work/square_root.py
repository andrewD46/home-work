#!/usr/bin/python3.8
# -*- coding: utf-8 -*-


def sqrt(number):
    if number == 0:
        return 0
    elif number > 0:
        t = number / 2.0
        g = t + 1
        while t != g:
            n = number / t
            g = t
            t = (t + n) / 2
        return t
    else:
        return 'ValueError: math domain error'


if __name__ == '__main__':
    user_number = float(input("Введите число: "))
    print(sqrt(user_number))
