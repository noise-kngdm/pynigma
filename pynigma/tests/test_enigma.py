import pytest
import instances as inst
import common
from plugboard import PlugBoard
from enigma import Enigma, EnigmaException


init_rotors = [
    [inst.ROTOR_I, inst.ROTOR_II, inst.ROTOR_III],
    [inst.ROTOR_II, inst.ROTOR_I, inst.ROTOR_IV],
    [inst.ROTOR_VII, inst.ROTOR_II, inst.ROTOR_IV],
]

init_positions = [
    [0, 3, 25],
    [10, 8, 2],
    [22, 22, 4],
]

init_reflector = [
    inst.REFLECTOR_B,
    inst.REFLECTOR_C,
]

init_plugboard = [
    PlugBoard([(x, x + 10) for x in range(1, 10)]),
    PlugBoard([]),
    PlugBoard([(1, 2), (3, 4), (5, 6)])
]


@pytest.mark.parametrize('rotors', init_rotors)
@pytest.mark.parametrize('positions', init_positions)
@pytest.mark.parametrize('reflector', init_reflector)
@pytest.mark.parametrize('plugboard', init_plugboard)
def test_enigma_init(rotors, positions, reflector, plugboard):
    Enigma(rotors, positions, reflector, plugboard)


@pytest.mark.parametrize('rotors,positions,reflector,plugboard', [
    (init_rotors[0]+[inst.ROTOR_I], [0, 3, 4, 5], inst.REFLECTOR_B,
     init_plugboard[0]),
    (init_rotors[1]*2, init_positions[0] * 2, inst.REFLECTOR_C,
     init_plugboard[0]),
    (init_rotors[2], init_positions[2], inst.REFLECTOR_C, 1),
    ])
def test_enigma_init_ko(rotors, positions, reflector, plugboard):
    with pytest.raises(EnigmaException):
        Enigma(rotors, positions, reflector, plugboard)


i_rotors = [inst.ROTOR_IV, inst.ROTOR_VI, inst.ROTOR_VIII, inst.ROTOR_BETA]


config_ringstellung = "EPEL"
for i in range(len(i_rotors)):
    i_rotors[i].ringstellung = ord(config_ringstellung[i])-ord('A')

plugboard = PlugBoard([(0, 4), (1, 5), (2, 12), (3, 16), (7, 20), (9, 13),
              (11, 23), (15, 17), (18, 25), (21, 22)])


usr_inp = """
Hola manin
"""

exp_outp = "PZTXCRYTB"


@pytest.mark.parametrize('rotors,positions,reflector,\
plugboard,user_input,expected_output', [
    (i_rotors, [4, 15, 4, 11], inst.REFLECTOR_C,
     plugboard, usr_inp, exp_outp),
    ])
@pytest.mark.xfail
def test_enigma_cipher(rotors, positions, reflector, plugboard,
                       user_input, expected_output):
    machine = Enigma(rotors, positions, reflector, plugboard)
    assert machine.cipher(user_input) == expected_output



rotors = [inst.ROTOR_I, inst.ROTOR_II, inst.ROTOR_III]

config_ringstellung = "AAA"
for i in range(len(rotors)):
    rotors[i].ringstellung = common.char_to_int(config_ringstellung[i])

plugboard = PlugBoard()
expected_output = "B"
user_input = "A"
expected_rotor_positions = [1, 0, 0]


@pytest.mark.parametrize('rotors,positions,reflector,\
plugboard,user_input,expected_output,expected_rotor_positions', [
    (rotors, [0, 0, 0], inst.REFLECTOR_B,
     plugboard, user_input, expected_output, expected_rotor_positions),
    ])
def test_enigma_rotor_positions(rotors, positions, reflector, plugboard,
                       user_input, expected_output,expected_rotor_positions):
    machine = Enigma(rotors, positions, reflector, plugboard)
    output = machine.cipher(user_input)
    for i in range(len(rotors)):    
        assert machine._permutation_block._rotor_positions[i] == \
            expected_rotor_positions[i]
    assert output == expected_output

expected_rotor_encrypt = [5, 3, 2]

rotors = [inst.ROTOR_I, inst.ROTOR_II, inst.ROTOR_III]

config_ringstellung = "AAA"
for i in range(len(rotors)):
    rotors[i].ringstellung = common.char_to_int(config_ringstellung[i])

plugboard = PlugBoard()
user_input = ["A", "H"]

@pytest.mark.parametrize('rotors,positions,reflector,\
plugboard,expected_rotor_encrypt,user_input', [
    (rotors, [0, 0, 0], inst.REFLECTOR_B,
     plugboard, expected_rotor_encrypt, user_input[0]),
    ])
def test_enigma_cipher_steps(rotors, positions, reflector, plugboard,
                       expected_rotor_encrypt, user_input):
    m = Enigma(rotors, positions, reflector, plugboard)
    output = m.cipher(user_input)
    for i in range(len(rotors)):
        assert m._permutation_block._rotors[i].cipher(common.char_to_int(user_input)) == expected_rotor_encrypt[i]


rotors = [inst.ROTOR_I, inst.ROTOR_II, inst.ROTOR_III]

config_ringstellung = "AAA"
for i in range(len(rotors)):
    rotors[i].ringstellung = common.char_to_int(config_ringstellung[i])

plugboard = PlugBoard()
expected_output = ["B", "I"]
user_input = ["A", "H"]


@pytest.mark.xfail
@pytest.mark.parametrize('user_input, expected_output', 
                         [(user_input[0], expected_output[0]),
                         (user_input[1], expected_output[1])
                         ])
@pytest.mark.parametrize('rotors,positions,reflector,\
plugboard,expected_rotor_encrypt', [
    (rotors, [0, 0, 0], inst.REFLECTOR_B,
     plugboard, expected_rotor_encrypt),
    ])
def test_enigma_cipher_char(rotors, positions, reflector, plugboard,
                       expected_rotor_encrypt, user_input, expected_output):
    m = Enigma(rotors, positions, reflector, plugboard)
    output = m.cipher(user_input)
    assert output == expected_output