def best_score(a_dictionary):
    size = len(a_dictionary)
    for i in range(size):
        if a_dictionary.values()[i] > a_dictionary.values()[i + 1]:
            best_sc = a_dictionary.values()[i]
        else:
            best_sc = a_dictionary.values()[i + 1]
    return (best_sc)
