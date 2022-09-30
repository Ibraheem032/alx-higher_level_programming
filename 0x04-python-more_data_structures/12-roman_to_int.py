#!/usr/bin/python3
def roman_to_int(roman_string):
    keys = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    values = [1, 5, 10, 50, 100, 500, 1000]
    my_list = []
    for k in roman_string:
        for i in range(7):
            if k == keys[i]:
                my_list.append(values[i])
    result = 0
    i = 0
    while i < len(my_list):
        if i < len(my_list) - 1:
            if my_list[i] < my_list[i + 1]:
                my_list[i] = -my_list[i]
        result = result + my_list[i]
        i = i + 1
    return (result)
