def readInputTextFile(filename):
    """Read input file(filename) and return list of int

    Arguments:
        filename {[string]} -- [name of input file]

    Returns:
        [list of int] -- [input list]
    """
    with open(filename, 'r') as f:
        int_list = list(map(int, f.readline().split(' ')))

    return int_list
