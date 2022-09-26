#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is False:
        a = 'None'
    else:
        a = sentence[0]
    ret = [len(sentence), a]
    return (tuple(ret))
