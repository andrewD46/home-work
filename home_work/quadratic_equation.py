#!/usr/bin/python3.8
# -*- coding: utf-8 -*-

import math

from decimal import Decimal


def get_roots(a, b, c):
    discriminant = (b ** 2) - 4 * a * c

    if a == 0:
        if b != 0:
            linear = -1 * c / b
            return linear

    if a == 0 or discriminant < 0:
        return "No solutions"

    if discriminant == 0:
        return -b / (2 * a)

    if discriminant > 0:
        first_root = (-b + Decimal(math.sqrt(discriminant))) / (2 * a)
        second_root = (-b - Decimal(math.sqrt(discriminant))) / (2 * a)
        return first_root, second_root


if __name__ == "__main__":
    first_coef = Decimal((input("Enter the first coefficient: ")))
    second_coef = Decimal((input('Enter the second coefficient: ')))
    third_coef = Decimal((input("Enter the third coefficient: ")))
    print(get_roots(first_coef, second_coef, third_coef))
