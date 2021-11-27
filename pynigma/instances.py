from rotor import Rotor
from reflector import Reflector
from common import char_to_int as cti
from common import str_to_tuples as strtt


class Rotors:
    _keys = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    @classmethod
    def rotor_i(cls):
        return Rotor({cti('Q')}, strtt(Rotors._keys, "EKMFLGDQVZNTOWYHXUSPAIBRCJ"))

    @classmethod
    def rotor_ii(cls):
        return Rotor({cti('E')}, strtt(Rotors._keys, "AJDKSIRUXBLHWTMCQGZNPYFVOE"))

    @classmethod
    def rotor_iii(cls):
        return Rotor({cti('V')}, strtt(Rotors._keys, "BDFHJLCPRTXVZNYEIWGAKMUSQO"))

    @classmethod
    def rotor_iv(cls):
        return Rotor({cti('J')}, strtt(Rotors._keys, "ESOVPZJAYQUIRHXLNFTGKDCMWB"))

    @classmethod
    def rotor_v(cls):
        return Rotor({cti('Z')}, strtt(Rotors._keys, "VZBRGITYUPSDNHLXAWMJQOFECK"))

    @classmethod
    def rotor_vi(cls):
        return Rotor({cti('Z'), cti('M')}, strtt(Rotors._keys, "JPGVOUMFYQBENHZRDKASXLICTW"))

    @classmethod
    def rotor_vii(cls):
        return Rotor({cti('Z'), cti('M')}, strtt(Rotors._keys, "NZJHGRCXMYSWBOUFAIVLPEKQDT"))

    @classmethod
    def rotor_viii(cls):
        return Rotor({cti('Z'), cti('M')}, strtt(Rotors._keys, "FKQHTLXOCBJSPDZRAMEWNIUYGV"))

    @classmethod
    def rotor_beta(cls):
        return Rotor({cti('A')}, strtt(Rotors._keys, "LEYJVCNIXWPBQMDRTAKZGFUHOS"), fixed=True)

    @classmethod
    def rotor_gamma(cls):
        return Rotor({cti('A')}, strtt(Rotors._keys, "FSOKANUERHMBTIYCWLQPZXVGJD"), fixed=True)


class Reflectors:
    _keys = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    @classmethod
    def reflector_b(cls):
        return Reflector(strtt(Reflectors._keys, "YRUHQSLDPXNGOKMIEBFZCWVJAT"))

    @classmethod
    def reflector_c(cls):
        return Reflector(strtt(Reflectors._keys, "FVPJIAOYEDRZXWGCTKUQSBNMHL"))

    @classmethod
    def reflector_b_thin(cls):
        return Reflector(strtt(Reflectors._keys, "ENKQAUYWJICOPBLMDXZVFTHRGS"))

    @classmethod
    def reflector_c_thin(cls):
        return Reflector(strtt(Reflectors._keys, "RDOBJNTKVEHMLFCWZAXGYIPSUQ"))
