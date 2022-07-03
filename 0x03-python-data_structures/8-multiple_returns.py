#!/usr/bin/python3
def multiple_returns(sentence):
    F_C = ''
    if sentence == "":
        return (len(sentence), None)
    else:
        F_C = sentence[0]
        return (len(sentence), F_C)
