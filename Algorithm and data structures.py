def linear_search(list, target):
    """Returns the index position of the target in the list, if found,else returns none."""

    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def verfy