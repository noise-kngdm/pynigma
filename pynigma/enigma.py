import sys
import re
import constants as ct
from rotor import Rotor
from plugboard import PlugBoard
from reflector import Reflector
from permutation_block import PermutationBlock


class EnigmaException(TypeError):
    pass


class Enigma:
    """Class that represents an enigma machine."""

    def __init__(self, rotors: list[Rotor], positions: list[int],
                 reflector: Reflector, plugboard: PlugBoard):
        """
        Constructor of the Enigma class.

        Parameters
        ----------
        rotors : list[Rotor]
            List of rotors used to cipher and decipher a message.
        positions : list[int]
            List with the initial position -grundstellung- of each rotor.
        reflector : Reflector
            Reflector used to cipher and decipher a message.
        """
        if len(rotors) not in ct.VALID_NUM_ROTORS:
            valid_nums = ' or '.join([str(x) for x in ct.VALID_NUM_ROTORS])
            raise(EnigmaException(f"{len(rotors)} is not a valid number of"
                                  f"rotors, please use {valid_nums} rotors"))

        self._permutation_block = PermutationBlock(rotors, positions,
                                                   reflector)

    @classmethod
    def normalize_string(cls, string: str) -> str:
        """
        Removes non-alphabetic characters from string and makes every
        character uppercase.

        Parameters
        ----------
        string : str
            The string that should be normalized.

        Returns
        -------
        str
            Normalized string
        """
        return re.sub(r'[^A-Z]', '', string.upper())

    def cipher(self, string: str) -> str:
        """
        Ciphers the string passed as parameter.

        Parameters
        ----------
        string : str
            String that should be ciphered.

        Returns
        -------
        str
            The string ciphered using the machine's state and configuration.
        """
        normalized_str = Enigma.normalize_string(string)
        ciphered_str = [ct.MIN_CHAR + self.cipher_char(ord(x) - ct.MIN_CHAR)
                        for x in normalized_str]

        return ''.join(ciphered_str)

    def cipher_char(self, char: str) -> str:
        """
        Ciphers the character passed as parameter.

        Parameters
        ----------
        character : str
            Character that should be ciphered.

        Returns
        -------
        str
            The character ciphered using the machine's state and configuration.
        """
        if len(char) != 1:
            raise EnigmaException(f"The {sys._getframe(1).f_code.co_name}"
                                  " method must be called using exactly "
                                  "1 parameter.")
        ciphered_char = self._plugboard.cipher(char)
        ciphered_char = self.permutation_block.cipher(ciphered_char)
        return self._plugboard.cipher(ciphered_char)
