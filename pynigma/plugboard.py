import sys
import constants
from collections import Counter

MAX_NUM_PAIRS = 10


class PlugBoard():
    def _check_valid_number(self, num: int):
        if num < constants.MIN_NUM or num > constants.MAX_NUM:
            raise ValueError(f'The value of {num} must be between '
                             f'{constants.MIN_NUM} and {constants.MAX_NUM}')

    def _check_non_double_keys(self, keys):
        occurences = Counter(keys)
        if occurences.most_common(1)[0][1] > 1:
            raise ValueError('You can only use each character once')

    def __init__(self, pairs: list[tuple[int, int]]):
        """
        Constructor of the PlugBoard class.

        Parameters
        ----------
        pairs : list[tuple[int]]
            A list with up to 10 tuples of numbers between 0 and 26.
        """
        if len(pairs) > MAX_NUM_PAIRS:
            raise TypeError('The max number of pairs that can be passed to'
                            f'{sys._getframe(1).f_code.co_name} is '
                            f'{MAX_NUM_PAIRS}')

        if len(pairs) > 0:
            self._check_non_double_keys([x[0] for x in pairs])
            self._check_non_double_keys([x[1] for x in pairs])

        self._permutations = {x: x for x in range(constants.MIN_NUM,
                                                  constants.MAX_NUM + 1)}
        for x, y in pairs:
            self._check_valid_number(x)
            self._check_valid_number(y)
            self._permutations[x] = y
            self._permutations[y] = x

    def cipher(self, num: int):
        """
        Returns the parameter ciphered.

        Parameters
        ----------
        num : int
            The ordinal corresponding to the character that should be ciphered.

        Returns
        -------
        int
            The ordinal corresponding to the ciphered parameter.
        """
        try:
            return self._permutations[num]
        except KeyError as e:
            raise KeyError('The value introduced is not valid, please, use '
                           f'a character between {constants.MIN_CHAR} and '
                           f'{constants.MAX_CHAR}') from e
