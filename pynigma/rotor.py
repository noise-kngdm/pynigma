import constants

class Rotor():
    """
    Module that represent a Rotor or Walzenlage
    """
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

    def __init__(self, ringstellung, grundstellung, permutations: list[list[int, int]]):
        """
            Constructor of the Rotor class.

            Parameters
            ----------
            ringstellung : str
                Letter that configure the rotor's ring
            grundstellung : str
                Letter that is configure to be the initial letter of the rotor
            permutations : list[tuple[int]]
                A nested list of numbers between in the [1-26] range, simulating a dictionary.

            Raises
            ------
            ValueError
                If the number of ringstellung is not in the expected range.
            ValueError
                If the number of grundstellung is not in the expected range.
            ValueError
                If permutation has more than 26 items
        """
        if len(permutations) > constants.MAX_NUM:
            raise TypeError('The max number of pairs that can be passed to'
                            f'{sys._getframe(1).f_code.co_name} is '
                            f'{constants.MAX_NUM_PAIRS_PLUGBOARD}')