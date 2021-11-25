import common
import constants
from base import Base


class Reflector(Base):
    """This class represents a reflector."""

    NUM_PERMUTATIONS = constants.NUM_CHARS

    def __init__(self, permutations: list[tuple[int, int]]):
        """
        Constructor of the Reflector class.

        Parameters
        ----------
        permutations : list[tuple[int, int]]
            A list with tuples of numbers between in the [1-26] range.
        """
        super().__init__(permutations)
        if len(permutations) != constants.NUM_CHARS:
            raise TypeError('The number of elements that must to be passed to '
                            f'the permutations list is '
                            f'{Reflector.NUM_PERMUTATIONS}')

    def _set_map(self, permutations: list[tuple[int, int]]):
        """
        Set the values of the _permutations attribute.

        Parameters
        ----------
        permutations : list[tuple[int, int]]
            A list with pairs of key and number it will be translated to.
        """
        for x, y in permutations:
            common.check_valid_number(x)
            common.check_valid_number(y)
            self._set_key(x, y)

    def _set_key(self, x: int, y: int):
        """
        Set the value of x in the _permutations map.

        Parameters
        ----------
        x : int
            A number.
        y : int
            A number.
        """
        self._permutations[x] = y
