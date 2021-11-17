import constants


def str_to_tuples(str1, str2):
    """
    Convert two strings into a list of tuples.

    Parameters
    ----------
    str1 : string
        A string which contains letters from 'A' to 'Z'.
    str2 : string
        A string which contains letters from 'A' to 'Z'.

    Returns
    -------
        r : list[tuple[int, int]]
            A list of tuples with numbers between in the [1-26] range.
    """
    r = [(ord(str1[i])-ord(constants.MIN_CHAR),
          ord(str2[i])-ord(constants.MIN_CHAR))
          for i in range(constants.MIN_NUM, constants.NUM_CHARS)]

    return r
