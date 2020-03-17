#!/usr/bin/python3.8
# -*- coding: utf-8 -*-

import psutil


def random_func(modulus=2 ** 32, a=1103515245, c=12345):
    """
    Линейный конгруэнтный генератор
    modulus - модуль
    а - умножитель
    с - приращение
    seed - начальное значение
    """
    seed = psutil.cpu_percent(interval=1)
    random_value = (a * seed + c) % modulus
    return random_value / modulus


if __name__ == "__main__":
    print('%.15f' % random_func())
