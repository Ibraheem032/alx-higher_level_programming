def best_score(a_dictionary):
    if a_dictionary:
        best_sc = max(a_dictionary.values())
        for i in a_dictionary.keys():
            if a_dictionary[i] == best_sc:
                return (i)
    else:
        return (None)
