#!/usr/bin/python3
def multiple_returns(sentence):
    Length = len(sentence)
    first = sentence[0] if len(sentence) > 0 else None
    return (Length, first)
