import pytest
import instances as inst
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
