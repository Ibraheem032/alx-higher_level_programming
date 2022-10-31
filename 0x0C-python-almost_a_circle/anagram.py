#!/usr/bin/python3
def swap(my_list, idx1, idx2):
    tmp = my_list[idx1]
    my_list[idx1] = my_list[idx2]
    my_list[idx2] = tmp
    return my_list

def anagramize(my_string):
    anagram = []
    my_list = []
    for l in my_string:
        my_list.append(l)
    tmp_list = [] + my_list
    list_len = len(my_list)
    for i in range(list_len):
        try:
            for j in range(i + 1, list_len):
                shuffled_list = swap(my_list, i, j)
                anagram.append(''.join(shuffled_list))
                my_list = tmp_list + []
        except IndexError:
            pass
    return anagram
def select(my_list, num):
    comb = num ** len(my_list)
    
    
for equ in anagramize('3+8*5'):
    try:
        print("{} = {}".format(equ, eval(equ)))
    except SyntaxError:
        pass
