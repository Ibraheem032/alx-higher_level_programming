#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return (str)
    start = str[0:n]
    end = str[n + 1:]
    new = start + end
    return (new)
