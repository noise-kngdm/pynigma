import common
import constants
from rotor import Rotor
from reflector import Reflector


class PermutationBlock:
    """A class that encapsulates the behavior and logic of a set of rotors
        -Walzen- and a reflector -Umkehrwalze-.
    """
    def __init__(self, rotors: list[Rotor], positions: list[int],
                 reflector: Reflector):
        """
        Constructor of the PermutationBlock class.

        Parameters
        ----------
        rotors : list[Rotor]
            List of rotors used to cipher and decipher a message.
        positions : list[int]
            List with the initial position -grundstellung- of each rotor.
        reflector : Reflector
            Reflector used to cipher and decipher a message.
        """
        if len(rotors) != len(positions):
            raise ValueError("The len of the rotors and positions lists must "
                             "be the same.")

        self._rotors = rotors
        for x in positions:
            common.check_valid_number(x)
        self._rotor_positions = positions
        self._reflector = reflector

    def _rotate_rotor(self, index: int):
        """
        Method that rotates the rotor whose index was specified as a parameter.

        Parameters
        ----------
        index : int
            Index of the rotor which should be rotated.
        """
        self._rotor_positions[index] = (self._rotor_positions[index] + 1) \
            % constants.NUM_CHARS

    def _cipher_stage(self, char: int, forward: bool = False) -> int:
        """
        Method that performs a sequence of ciphers from one end of the rotor
         list to the other.

        Parameters
        ----------
        char : int
            Character that will be ciphered.
        forward : bool
            If the cipher stage is from the start of the rotors to the
             reflector -forward- or from the reflector to the start -backward-.

        Returns
        -------
        int
            The result of ciphering the input in this stage.
        """
        # The first rotor must always be rotated in the forward stage
        cipher_char = char
        order = range(len(self._rotors))
        order = order if forward else reversed(order)

        for i in order:
            cipher_char = self._rotors[i].cipher(
                cipher_char + self._rotor_positions[i] % constants.NUM_CHARS
            )

        return cipher_char

    def _prepare_rotors(self):
        """
        Method that rotates every rotor that needs to be rotated.
        """
        def set_rotate(index: int):
            nonlocal must_rotate
            if self._rotors[i].must_rotate_next_rotor(
                    self._rotor_positions[i]):
                must_rotate[i+1] = True

        must_rotate = [False] * len(self._rotors)
        must_rotate[0] = True
        for i in range(len(self._rotors) - 1):
            if not self._rotors[i+1].fixed:
                set_rotate(i)

        if must_rotate[2]:
            # Double stepping
            must_rotate[1] = True

        for i in len(self._rotors):
            if must_rotate[i]:
                self._rotate_rotor(i)

    def cipher(self, char: int) -> int:
        """
        Returns the parameter ciphered.

        Parameters
        ----------
        char : int
            The ordinal corresponding to the character that should be ciphered.

        Returns
        -------
        int
            The ordinal corresponding to the ciphered parameter.
        """
        self._prepare_rotors()
        ciphered_char = self._cipher_stage(char, True)
        ciphered_char = self._reflector.cipher(ciphered_char)
        return self._cipher_stage(ciphered_char)
