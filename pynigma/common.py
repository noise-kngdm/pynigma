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


def check_valid_number(num: int):
    """
    Checks that the number passed as a parameter is a valid one.
     Parameters
    ----------
    num : int
        Number that will be checked.
    Raises
    ------
    ValueError
        If the number is not in the expected range.
    """
    if num < constants.MIN_NUM or num > constants.MAX_NUM:
        raise ValueError(f'The value of {num} must be between '
                         f'{constants.MIN_NUM} and {constants.MAX_NUM}')
