#!/usr/bin/python3.8
# -*- coding: utf-8 -*-


def mystery(size):
    start_arr = [bin(i) for i in range(0, 2 ** size)]
    encoded_arr = []

    # print([(bin(i)[2:].zfill(size)) for i in range(0, 2 ** size)])

    for i in start_arr:
        i = (int(i, 2) ^ (int(i, 2) >> 1))
        encoded_arr.append(bin(i))

    return start_arr, encoded_arr, int(encoded_arr[size], 2)


def mystery_inv(number, array):
    for i, el in enumerate(array):
        if el == bin(number):
            return i
    return "No item"


if __name__ == "__main__":
    user_number = int(input("Введите число n: "))
    first_arr, second_arr, number_pos = mystery(user_number)
    print(first_arr)
    print(second_arr)
    print(number_pos)
    array_number = int(input("Введите число массива: "))
    print(mystery_inv(array_number, second_arr))
