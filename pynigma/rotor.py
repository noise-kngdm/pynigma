import constants
import common
from base import Base


class Rotor(Base):
    """
    Module that represent a Rotor or Walzenlage
    """
    NUM_PERMUTATIONS = constants.NUM_CHARS

    def __init__(self, notch, permutations, ringstellung=0, fixed=False):
        """
            Constructor of the Rotor class.

            Parameters
            ----------
            ringstellung : int
                Number that equals to a letter that configure the rotor's ring.
            notch : set of int
                Set of int which this function uses to indicate to the next
                rotor to rotate.
            permutations : list[tuple[int, int]]
                A list of tuples with numbers between in the [1-26] range.
            fixed : Boolean
                A boolean which indicates if the rotor can rotate or not.

            Raises
            ------
            ValueError
                If the number of ringstellung is not in the expected range.
            ValueError
                If the set of grundstellung is not in the expected range.
            ValueError
                If notch has more than 26 items.
            ValueError
                If permutation has more than 26 items.
        """
        for i in notch:
            common.check_valid_number(i)
        self._notch = notch
        common.check_valid_number(ringstellung)
        self._ringstellung = ringstellung
        super().__init__(permutations)
        self._fixed = fixed

        if len(notch) < constants.MIN_NUM+1 or \
           len(notch) > constants.NUM_CHARS:
            raise TypeError('The number of elements that must to be passed to '
                            'the notch list is not appropiated')

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
        common.check_valid_number(ringstellung)
        self._ringstellung = ringstellung
        temp_copy = self._permutations.copy()
        for i in range(constants.MIN_NUM, constants.NUM_CHARS):
            new_pos = (i - self._ringstellung) % constants.NUM_CHARS
            self._permutations[i] = (temp_copy[new_pos] + self._ringstellung) % constants.NUM_CHARS
        self._set_rev_permutations()

    def _set_map(self, permutations: list[tuple[int, int]]):
        for i in range(constants.MIN_NUM, constants.NUM_CHARS):
            x = permutations[i][0]
            new_pos = (i + self._ringstellung) % constants.NUM_CHARS
            y = (permutations[new_pos][1] + self._ringstellung) % constants.NUM_CHARS
            common.check_valid_number(x)
            common.check_valid_number(y)
            self._set_key(x, y)

    def must_rotate_next_rotor(self, pos):
        """
        Check if the next rotor has to rotate.

        Parameters
        ----------
        pos : int
            A number which indicates the position of the rotor.
        """
        return pos in self._notch

    @property
    def fixed(self):
        """If the rotor is movable or not."""
        return self._fixed
