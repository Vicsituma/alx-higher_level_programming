#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) == 0 or a_dictionary is None:
        return None
    w = (a_dictionary.values())
    x = (a_dictionary.keys())
    return x[w.index(max(w))]
