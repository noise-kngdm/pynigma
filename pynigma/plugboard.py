import sys
import pynigma.constants as constants
import pynigma.common as common
from pynigma.base import Base


class PlugBoard(Base):
    """
    Module that represents the PlugBoard or Steckerbrett.
    """
    NUM_PERMUTATIONS = constants.MAX_NUM_PAIRS_PLUGBOARD

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
        super()._check_keys_and_values(keys, values)

        for x in keys:
            if x in values:
                raise ValueError('You can only use each character once for '
                                 'each permutation')

    def __init__(self, pairs=[]):
        """
        Constructor of the PlugBoard class.

        Parameters
        ----------
        pairs : list[tuple[int, int]]
            A list with up to 10 tuples of numbers between in the [0-25] range.

        Raises
        ------
        ValueError
            If a number was used more than once.
        ValueError
            If a number is not in the expected range.
        """
        super().__init__(pairs)

        if len(pairs) > constants.MAX_NUM_PAIRS_PLUGBOARD:
            raise TypeError('The max number of pairs that can be passed to'
                            f'{sys._getframe(1).f_code.co_name} is '
                            f'{constants.MAX_NUM_PAIRS_PLUGBOARD}')

    def _set_map(self, permutations: list[tuple[int, int]]):
        for x, y in permutations:
            common.check_valid_number(x)
            common.check_valid_number(y)
            self._set_key(x, y)

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
        self._permutations[x] = y
        self._permutations[y] = x
