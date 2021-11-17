import rotor
import reflector
import constants
import common


keys = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Defining Rotor I
values_1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
notch = {ord('Q')-ord(constants.MIN_CHAR)}
ROTOR_I = rotor.Rotor(notch, common.str_to_tuples(keys, values_1))

# Defining Rotor II
values_2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
notch = {ord('E')-ord(constants.MIN_CHAR)}
ROTOR_II = rotor.Rotor(notch, common.str_to_tuples(keys, values_2))

# Defining Rotor III
values_3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
notch = {ord('V')-ord(constants.MIN_CHAR)}
ROTOR_III = rotor.Rotor(notch, common.str_to_tuples(keys, values_3))

# Defining Rotor IV
values_4 = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
notch = {ord('J')-ord(constants.MIN_CHAR)}
ROTOR_IV = rotor.Rotor(notch, common.str_to_tuples(keys, values_4))

# Defining Rotor V
values_5 = "VZBRGITYUPSDNHLXAWMJQOFECK"
notch = {ord('Z')-ord(constants.MIN_CHAR)}
ROTOR_V = rotor.Rotor(notch, common.str_to_tuples(keys, values_5))

# Defining Rotor VI
values_6 = "JPGVOUMFYQBENHZRDKASXLICTW"
notch = {ord('Z')-ord(constants.MIN_CHAR), ord('M')-ord(constants.MIN_CHAR)}
ROTOR_VI = rotor.Rotor(notch, common.str_to_tuples(keys, values_6))

# Defining Rotor VII
values_7 = "NZJHGRCXMYSWBOUFAIVLPEKQDT"
notch = {ord('Z')-ord(constants.MIN_CHAR), ord('M')-ord(constants.MIN_CHAR)}
ROTOR_VII = rotor.Rotor(notch, common.str_to_tuples(keys, values_7))

# Defining Rotor VIII
values_8 = "FKQHTLXOCBJSPDZRAMEWNIUYGV"
notch = {ord('Z')-ord(constants.MIN_CHAR), ord('M')-ord(constants.MIN_CHAR)}
ROTOR_VIII = rotor.Rotor(notch, common.str_to_tuples(keys, values_8))

# Defining Beta rotor
values_beta = "LEYJVCNIXWPBQMDRTAKZGFUHOS"
notch = {ord('A')-ord(constants.MIN_CHAR)}
ROTOR_BETA = rotor.Rotor(notch, common.str_to_tuples(keys, values_beta),
                         0, True)

# Defining Gamma rotor
values_gamma = "LEYJVCNIXWPBQMDRTAKZGFUHOS"
notch = {ord('A')-ord(constants.MIN_CHAR)}
ROTOR_GAMMA = rotor.Rotor(notch, common.str_to_tuples(keys, values_gamma),
                          0, True)

# Defining B reflector
values_b = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
REFLECTOR_B = reflector.Reflector(common.str_to_tuples(keys, values_b))

# Defining C reflector
values_c = "FVPJIAOYEDRZXWGCTKUQSBNMHL"
REFLECTOR_C = reflector.Reflector(common.str_to_tuples(keys, values_c))

# Defining B thin reflector
values_b_thin = "ENKQAUYWJICOPBLMDXZVFTHRGS"
REFLECTOR_B_thin = reflector.Reflector(common.str_to_tuples(keys, values_b_thin))

# Defining C thin reflector
values_c_thin = "RDOBJNTKVEHMLFCWZAXGYIPSUQ"
REFLECTOR_C_thin = reflector.Reflector(common.str_to_tuples(keys, values_c_thin))
