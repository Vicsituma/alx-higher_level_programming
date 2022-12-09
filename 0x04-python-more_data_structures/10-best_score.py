#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    w = list(a_dictionary.values())
    x = list(a_dictionary.keys())
    return x[w.index(max(w))]
