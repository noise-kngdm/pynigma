import sys
import constants
from typing import List
from base_enigma import Base


class Rotor(Base):
    """
    Module that represent a Rotor or Walzenlage
    """
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

    def __init__(self, ringstellung, grundstellung, notch, permutations):
        """
            Constructor of the Rotor class.

            Parameters
            ----------
            ringstellung : int
                Number that equals to a letter that configure the rotor's ring
            grundstellung : int
                Number that equals to a letter that is configure to be the initial letter of the rotor
            notch : int
                Number which his function is to indicate to his left rotor to do a rotation
            permutations : list[tuple[int, int]]
                A list of tuples with numbers between in the [1-26] range.

            Raises
            ------
            ValueError
                If the number of ringstellung is not in the expected range.
            ValueError
                If the number of grundstellung is not in the expected range.
            ValueError
                If permutation has more than 26 items
        """
        super().__init__(permutations)

        if len(permutations) != constants.MAX_NUM:
            raise TypeError('The number of elements that must to be passed to'
                            f'{sys._getframe(4).f_code.co_name} is '
                            f'{constants.MAX_NUM}')

        self._check_valid_number(ringstellung)
        self._ringstellung = ringstellung
    
        self._check_valid_number(notch)
        self._notch = notch

        self._check_valid_number(grundstellung)
        self._grundstellung = grundstellung

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

def num_of(cad):
        return ord(cad)-ord('A') + 1

if __name__ == '__main__':

    k = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    l = "ZYXWVUTSRQPONMLKJIHGFEDCBA"

    lista = [(num_of(k[i]),num_of(l[i])) for i in range(constants.MAX_NUM)]
            
    print(lista)

    rotor_1 = Rotor(10,10,10,lista)