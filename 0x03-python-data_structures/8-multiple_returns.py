#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        a = 'None'
    else:
        a = sentence[0]
    ret = [len(sentence), a]
    return (tuple(ret))
