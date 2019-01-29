def deleteOutlier(int_list):
    """Delelte outlier (not 10-20) int

    Arguments:
        int_list {[list of int]} -- [input list]

    Returns:
        [list of int] -- [outlier deleted list]
    """

    modified_list = []
    for i in int_list:
        if (i <10 or i>20):
            pass
        else:
            modified_list.append(i)

    return modified_list
