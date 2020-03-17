#!/usr/bin/python3.8
# -*- coding: utf-8 -*-

# print([(bin(i)[2:].zfill(size)) for i in range(0, 2 ** size)])


def is_divisible(number):
    amount = 8
    j = 0
    while amount > 7:
        arr = []
        number_arr = []
        number = str(bin(number)[2:])
        print("number = ", number)
        number_len = str(bin(len(number))[2:])
        print("number_len = ", number_len)
        # if int(number_len, 2) != 3 and number_len[-1] == "1":
        #     number = "0" + str(number)
        # print("number + 0 = ", number)

        # print("number in arr = ", number_arr)

        while True:
            print("j = ", j)
            number_arr = [number[x:x + 3] for x in range(0, len(number), 3)]
            print("arr 3 = ", number_arr)
            if len(number_arr[j]) == 3:
                j += 1
            elif len(number_arr[j]) != 3:
                number = "0" + number
                j = 0
                print("в цикле: ", number)
            if len(number_arr[-1]) == 3:
                break

        print("new number in arr = ", number)
        for i in number_arr:
            a = "0b" + i
            arr.append(a)
        print("arr = ", arr)
        amount = sum((int(arr[i], 2) for i in range(0, len(arr))))
        print("amount = ", amount)
        if amount == 0b111:
            return True
        elif amount > 0b111:
            number = amount
        else:
            return False


if __name__ == "__main__":
    user_number = int(input("Введите число: "))
    print(is_divisible(user_number))
