import sys
import constants
from collections import Counter


class Base:
    """
    Module that contains some common methods/attributes
    and will be useful for inheritance.
    """
    def __init__(self, permutations: list[tuple[int, int]]):
        """
        Constructor of the Base class.

        Parameters
        ----------
        pairs : list[tuple[int, int]]
            A list with tuples of numbers between in the [1-26] range.
        """
        self._permutations = {x: x for x in range(constants.MIN_NUM,
                                                  constants.MAX_NUM + 1)}

        for x, y in permutations:
            self._check_valid_number(x)
            self._check_valid_number(y)                                        
            self._set_key(x,y)

        if len(permutations) > 0:
            self._check_keys_and_values([x[0] for x in permutations],
                                        [x[1] for x in permutations])


    def _set_key(self, x: int, y: int):
        """
        Set the values on _permutations.

        Parameters
        ----------
        x : int
            A number.
        y : int
            A number.
        """
        raise NotImplementedError

    def _check_valid_number(self, num: int):
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

    def _check_once_in_list(self, keys):
        occurences = Counter(keys)
        if occurences.most_common(1)[0][1] > 1:
            raise ValueError('You can only use each character once')

    def _check_keys_and_values(self, keys, values):
        """
        Check that no key was used twice, either as a key or as a value.

        Parameters
        ----------
        keys : list of int
            A list with all the keys used.
        values : list of int
            A list with all the values used.

        Raises
        ------
        ValueError
            If a number was used more than once.
        """
        self._check_once_in_list(keys)
        self._check_once_in_list(values) 
                                      