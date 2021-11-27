import sys
import re
from collections import Counter
import pynigma.constants as ct
import pynigma.common as common
from pynigma.rotor import Rotor
from pynigma.plugboard import PlugBoard
from pynigma.reflector import Reflector
from pynigma.permutation_block import PermutationBlock


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
        if not isinstance(plugboard, PlugBoard):
            raise(EnigmaException("The parameter plugboard must be an"
                                  " instance of the PlugBoard class"))
        self._plugboard = plugboard

        if len(rotors) not in ct.VALID_NUM_ROTORS:
            valid_nums = ' or '.join([str(x) for x in ct.VALID_NUM_ROTORS])
            raise(EnigmaException(f"{len(rotors)} is not a valid number of"
                                  f"rotors, please use {valid_nums} rotors"))
        occurences = Counter(rotors)
        if occurences.most_common(1)[0][1] > 1:
            raise EnigmaException('You can only use each rotor once')

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
            Normalized string.
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
        ciphered_str = [common.int_to_char(self.cipher_char(common.char_to_int(x)))
                        for x in normalized_str]

        return ''.join(ciphered_str)

    def cipher_char(self, char: int) -> int:
        """
        Ciphers the character passed as parameter.

        Parameters
        ----------
        char : int
            Character that should be ciphered.

        Returns
        -------
        int
            The character ciphered using the machine's state and configuration.
        """
        ciphered_char = self._plugboard.cipher(char)
        ciphered_char = self._permutation_block.cipher(ciphered_char)
        return self._plugboard.cipher(ciphered_char, False)
