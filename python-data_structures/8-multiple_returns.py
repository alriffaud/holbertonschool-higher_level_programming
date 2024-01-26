#!/usr/bin/python3
def multiple_returns(sentence):
    """
    This function returns a tuple with the length of a string and its first
    character.
    """
    if sentence == "":
        tuple_sentence = (0,"None")
    else:
        tuple_sentence = (len(sentence), sentence[0])
    return (tuple_sentence)
