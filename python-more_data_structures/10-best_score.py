#!/usr/bin/python3
def best_score(a_dictionary):
    """
    This function returns a key with the biggest integer value.
    """
    if a_dictionary is None or not a_dictionary:
        return (None)
    best = max(a_dictionary, key=a_dictionary.get)
    return (best)
