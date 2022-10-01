#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        total_score_sum = sum([i[0] * i[1] for i in my_list])
        sc_size = sum([i[1] for i in my_list])
        return (total_score_sum / sc_size)
    else:
        return (0)
