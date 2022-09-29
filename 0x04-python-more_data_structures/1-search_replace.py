#!/usr/bin/python3
def search_replace(my_ist, search, replace):
    new_list = [ i for i in my_list] 
    for j in range(0, len(new_list)):
        if new_list[j] == search:
            new_list[j] = replace
    return (new_list)
