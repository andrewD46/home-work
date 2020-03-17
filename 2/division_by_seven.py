#!/usr/bin/python3.8
# -*- coding: utf-8 -*-


def is_divisible(number):
    amount = 8
    while amount > 7:
        arr = []
        j = 0
        number = str(bin(number)[2:])

        number_arr = [number[x:x + 3] for x in range(0, len(number), 3)]
        if len(number_arr[-1]) == 1:
            number = "00" + number

        if len(number_arr[-1]) == 2:
            number = "0" + number

        number_arr = [number[x:x + 3] for x in range(0, len(number), 3)]
        for i in number_arr:
            a = "0b" + i
            arr.append(a)

        amount = sum((int(arr[i], 2) for i in range(0, len(arr))))
        if amount == 0b111:
            return True
        elif amount > 0b111:
            number = amount
        else:
            return False


if __name__ == "__main__":
    user_number = int(input("Введите число: "))
    print(is_divisible(user_number))
