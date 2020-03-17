#!/usr/bin/python3.8
# -*- coding: utf-8 -*-


def mystery(size):
    desired_num = 0
    coded_array = []

    for i in range(2 ** size):
        number = (i ^ (i >> 1))
        if size == i:
            desired_num = number

        coded_array.append(number)

    return desired_num, coded_array


def mystery_inv(number, array_numbers):
    for i, el in enumerate(array_numbers):
        if number == el:
            return i
    return "No item"


if __name__ == "__main__":
    user_number = int(input("Введите число n: "))
    number_pos, array = mystery(user_number)
    print(number_pos)
    array_number = int(input("Введите число в массиве: "))
    print(mystery_inv(array_number, array))
