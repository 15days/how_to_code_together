import sys
from readInputTextFile import readInputTextFile
from deleteOutlier import deleteOutlier
from remainOddOrEven import remainOddOrEven
from countNumOfUnique import countNumOfUnique

def myOwnCounter(filename):
    """Our Final Function

    Arguments:
        filename {[string]} -- [input file name]

    Returns:
        [int] -- [result]
    """
    tmp = readInputTextFile(filename)
    tmp = deleteOutlier(tmp)
    tmp = remainOddOrEven(tmp)
    num_of_uniq = countNumOfUnique(tmp)

    return num_of_uniq

if __name__ == '__main__':
    if len(sys.argv) == 1:
        filename = "input_ex.txt"
    else:
        filename = sys.argv[1]
    print("Answer is {}".format(myOwnCounter(filename)))
