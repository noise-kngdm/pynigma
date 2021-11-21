import sys
import re
from collections import Counter
import constants as ct
import common
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
        with open('/tmp/lol', 'a') as f:
            f.write(f'Aprendiendo before plugboard: {char}\n')
        ciphered_char = self._plugboard.cipher(char)
        with open('/tmp/lol', 'a') as f:
            f.write(f'Aprendiendo after plugboard: {ciphered_char}\n')
        ciphered_char = self._permutation_block.cipher(ciphered_char)
        with open('/tmp/lol', 'a') as f:
            f.write(f'Aprendiendo after permutation block: {ciphered_char}\n')
        return self._plugboard.cipher(ciphered_char)
