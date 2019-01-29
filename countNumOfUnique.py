def countNumOfUnique(int_list):
    """Count number of diff int

    Arguments:
        int_list {[list of int]} -- [only odd or even ints]

    Returns:
        [int] -- [number of diff int]
    """
    num_of_uniq = len(list(set(int_list)))

    return num_of_uniq
