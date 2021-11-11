import sys
import constants
from collections import Counter
from base_enigma import Base

class PlugBoard(Base):
    """
    Module that represents the PlugBoard or Steckerbrett.
    """
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
                                 

    def __init__(self, pairs: list[tuple[int, int]]):
        """
        Constructor of the PlugBoard class.

        Parameters
        ----------
        pairs : list[tuple[int, int]]
            A list with up to 10 tuples of numbers between in the [1-26] range.

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
