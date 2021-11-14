import constants
from base_enigma import Base


class Rotor(Base):
    """
    Module that represent a Rotor or Walzenlage
    """
    NUM_PERMUTATIONS = constants.NUM_CHARS

    def _check_keys_and_values(self, keys, values):
        """
        Check that a key's value is not equal to the key.

        Parameters
        ----------
        keys : list of int
            A list with all the keys used.
        values : list of int
            A list with all the values used.

        Raises
        ------
        ValueError
            If a key's value is equal to the key.
        ValueError
            If the number is not in the expected range.
        """
        super()._check_keys_and_values(keys, values)

        for i in range(len(keys)):
            if keys[i] == values[i]:
                raise ValueError('Key and value cannot be equal')

    def __init__(self, notch, permutations, ringstellung=0):
        """
            Constructor of the Rotor class.

            Parameters
            ----------
            ringstellung : int
                Number that equals to a letter that configure the rotor's ring.
            notch : set of int
                Set of int which this function uses to indicate to the next rotor
                to do a rotation.
            permutations : list[tuple[int, int]]
                A list of tuples with numbers between in the [1-26] range.

            Raises
            ------
            ValueError
                If the number of ringstellung is not in the expected range.
            ValueError
                If the set of grundstellung is not in the expected range.
            ValueError
                If notch has more than 26 items
            ValueError
                If permutation has more than 26 items
        """
        for i in notch:
            self._check_valid_number(i)
        self._notch = notch
        self._check_valid_number(ringstellung)
        self._ringstellung = ringstellung
        super().__init__(permutations)

        if len(notch) == constants.MIN_NUM+1 or len(notch) > constants.NUM_CHARS:
            raise TypeError('The number of elements that must to be passed to '
                            f'the notch list is not appropiated')

        if len(permutations) != constants.NUM_CHARS:
            raise TypeError('The number of elements that must to be passed to '
                            f'the permutations list is '
                            f'{Rotor.NUM_PERMUTATIONS}')

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

    @property
    def ringstellung(self):
        """Ringstellung of the rotor."""
        return self._ringstellung

    @ringstellung.setter
    def ringstellung(self, ringstellung):
        self._check_valid_number(ringstellung)
        self._ringstellung = ringstellung
        temp_copy = self._permutations.copy()
        for i in range(constants.MIN_NUM, constants.NUM_CHARS):
            new_pos = (i+self._ringstellung) % constants.NUM_CHARS
            self._permutations[i] = temp_copy[new_pos]

    def _set_map(self, permutations: list[tuple[int, int]]):
        for i in range(constants.MIN_NUM, constants.NUM_CHARS):
            x = permutations[i][0]
            new_pos = (i + self._ringstellung) % constants.NUM_CHARS
            y = permutations[new_pos][1]
            self._check_valid_number(x)
            self._check_valid_number(y)
            self._set_key(x, y)
