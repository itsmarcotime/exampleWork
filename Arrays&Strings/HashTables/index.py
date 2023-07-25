
def first_recurring(given_string):
    counts = {}

    for i in given_string:
        if i in counts:
            return i
        counts[i] = 1
    return None

given_string = "DBCABA"