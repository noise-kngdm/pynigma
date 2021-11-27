import pynigma.constants as constants
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
        permutations : list[tuple[int, int]]
            A list with tuples of numbers between in the [1-26] range.
        """
        self._permutations = {x: x for x in range(constants.MIN_NUM,
                                                  constants.NUM_CHARS)}
        self._set_map(permutations)
        self._set_rev_permutations()

        if len(permutations) > 0:
            self._check_keys_and_values([x[0] for x in permutations],
                                        [x[1] for x in permutations])

    def _set_rev_permutations(self):
        self._rev_permutations = {
            y: x for x, y in
               [(list(self._permutations.keys())[i], list(self._permutations.values())[i])
                for i in range(len(self._permutations))]
        }

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

    def _set_map(self, permutations: list[tuple[int, int]]):
        """
        Set the _permutations map.

        Parameters
        ----------
        permutations : list[tuple[int, int]]
            A list with tuples of numbers between in the [1-26] range.
        """
        raise NotImplementedError

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

    def cipher(self, num: int, forward=False):
        """
        Returns the parameter ciphered.

        Parameters
        ----------
        num : int
            The ordinal corresponding to the character that should be ciphered.
        forward : bool
            If the ciphering direction is forward.

        Returns
        -------
        int
            The ordinal corresponding to the ciphered parameter.
        """
        try:
            if forward:
                return self._permutations[num]
            else:
                return self._rev_permutations[num]
        except KeyError as e:
            raise KeyError('The value introduced is not valid, please, use '
                           f'a character between {constants.MIN_CHAR} and '
                           f'{constants.MAX_CHAR}') from e
