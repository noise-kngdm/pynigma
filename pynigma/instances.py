from rotor import Rotor
from reflector import Reflector
from common import char_to_int as cti
from common import str_to_tuples as strtt


class Rotors:
    _keys = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    @classmethod
    def ROTOR_I(cls):
        return Rotor({cti('Q')}, strtt(Rotors._keys, "EKMFLGDQVZNTOWYHXUSPAIBRCJ"))

    @classmethod
    def ROTOR_II(cls):
        return Rotor({cti('E')}, strtt(Rotors._keys, "AJDKSIRUXBLHWTMCQGZNPYFVOE"))

    @classmethod
    def ROTOR_III(cls):
        return Rotor({cti('V')}, strtt(Rotors._keys, "BDFHJLCPRTXVZNYEIWGAKMUSQO"))

    @classmethod
    def ROTOR_IV(cls):
        return Rotor({cti('J')}, strtt(Rotors._keys, "ESOVPZJAYQUIRHXLNFTGKDCMWB"))

    @classmethod
    def ROTOR_V(cls):
        return Rotor({cti('Z')}, strtt(Rotors._keys, "VZBRGITYUPSDNHLXAWMJQOFECK"))

    @classmethod
    def ROTOR_VI(cls):
        return Rotor({cti('Z'), cti('M')}, strtt(Rotors._keys, "JPGVOUMFYQBENHZRDKASXLICTW"))

    @classmethod
    def ROTOR_VII(cls):
        return Rotor({cti('Z'), cti('M')}, strtt(Rotors._keys, "NZJHGRCXMYSWBOUFAIVLPEKQDT"))

    @classmethod
    def ROTOR_VIII(cls):
        return Rotor({cti('Z'), cti('M')}, strtt(Rotors._keys, "FKQHTLXOCBJSPDZRAMEWNIUYGV"))

    @classmethod
    def ROTOR_BETA(cls):
        return Rotor({cti('A')}, strtt(Rotors._keys, "LEYJVCNIXWPBQMDRTAKZGFUHOS"), fixed=True)

    @classmethod
    def ROTOR_GAMMA(cls):
        return Rotor({cti('A')}, strtt(Rotors._keys, "LEYJVCNIXWPBQMDRTAKZGFUHOS"), fixed=True)


class Reflectors:
    _keys = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    @classmethod
    def REFLECTOR_B(cls):
        return Reflector(strtt(Reflectors._keys, "YRUHQSLDPXNGOKMIEBFZCWVJAT"))

    @classmethod
    def REFLECTOR_C(cls):
        return Reflector(strtt(Reflectors._keys, "FVPJIAOYEDRZXWGCTKUQSBNMHL"))

    @classmethod
    def REFLECTOR_B_thin(cls):
        return Reflector(strtt(Reflectors._keys, "ENKQAUYWJICOPBLMDXZVFTHRGS"))

    @classmethod
    def REFLECTOR_C_thin(cls):
        return Reflector(strtt(Reflectors._keys, "RDOBJNTKVEHMLFCWZAXGYIPSUQ"))
