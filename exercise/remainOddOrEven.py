def remainOddOrEven(int_list):
    """Delete odd or even int by length of list

    Arguments:
        int_list {[list of int]} -- [outlier deleted list]

    Returns:
        [list of int] -- [only odd or even ints]
    """

    if len(int_list) % 2 == 0:
        modified_list = [int for int in int_list if int % 2 == 0]
    else:
        modified_list = [int for int in int_list if int % 2 != 0]

    return modified_list
