import pytest
import pynigma.rotor
import pynigma.constants as constants

init_vals = [
    [(x, (x + 1) % (constants.NUM_CHARS)) for x in range(constants.MIN_NUM,
                                                         constants.NUM_CHARS)],
    [(x, (x + 5) % (constants.NUM_CHARS)) for x in range(constants.MIN_NUM,
                                                         constants.NUM_CHARS)]
]

ringstellung = [2, 13]
notch = {3, 10}


@pytest.mark.parametrize('test_list, ringstu, notch',
                            [(tuple(init_vals[0]), ringstellung[0], notch)]
                        )
def test_rotor_init(notch, test_list, ringstu):
    pynigma.rotor.Rotor(notch, test_list, ringstu)


expected_map = [{0: 3, 1: 4, 2: 5, 3: 6, 4: 7, 5: 8, 6: 9, 7: 10, 8: 11, 9: 12,
                 10: 13, 11: 14, 12: 15, 13: 16, 14: 17, 15: 18, 16: 19,
                 17: 20, 18: 21, 19: 22, 20: 23, 21: 24, 22: 25, 23: 0, 24: 1,
                 25: 2},

                {0: 18, 1: 19, 2: 20, 3: 21, 4: 22, 5: 23, 6: 24, 7: 25, 8: 0,
                 9: 1, 10: 2, 11: 3, 12: 4, 13: 5, 14: 6, 15: 7, 16: 8, 17: 9,
                 18: 10, 19: 11, 20: 12, 21: 13, 22: 14, 23: 15, 24: 16, 25: 17
                 }]


@pytest.mark.parametrize('test_list,ringstellung,expected_map', [
    (init_vals[0], ringstellung[0], expected_map[0]),
    (init_vals[1], ringstellung[1], expected_map[1])
    ])
def test_rotor_ringstellung(test_list, expected_map, ringstellung):
    rotor = pynigma.rotor.Rotor(notch, test_list, ringstellung)
    assert rotor._permutations == expected_map


@pytest.mark.parametrize('test_list,ringstellung,expected_map',
                         [(init_vals[0], ringstellung[0], expected_map[0]),
                          (init_vals[1], ringstellung[1], expected_map[1])
                          ])
def test_rotor_set_ringstellung(test_list, ringstellung, expected_map):
    rotor = pynigma.rotor.Rotor(notch, test_list)
    rotor.ringstellung = ringstellung
    assert rotor._permutations == expected_map


@pytest.mark.parametrize('init_vals,ringstellung,notch,', [
    ([1, 2], 0, 3),
    ([(x, x + 1000) for x in range(constants.NUM_CHARS)], 0, 3),
    ([(x, -2) for x in range(constants.NUM_CHARS)], 0, 3),
    ([(x, -2) for x in range(99)], 0, 3),
    ([], 0, 4),
    (init_vals[0], -1, 0),
    (init_vals[0], 10, -1)
])
def test_rotor_init_ko(init_vals, ringstellung, notch):
    with pytest.raises(Exception):
        pynigma.rotor.Rotor(notch, init_vals, ringstellung)

@pytest.mark.parametrize('test_list, ringstu, notch, user_input, expected_output',
                         [
                          (tuple(init_vals[0]), ringstellung[0], notch, 1, 4),
                          (tuple(init_vals[0]), ringstellung[0], notch, 25, 2),
                          (tuple(init_vals[1]), ringstellung[0], notch, 1, 8),
                          (tuple(init_vals[1]), ringstellung[0], notch, 25, 6)
                         ])
def test_rotor_cipher(notch, test_list, ringstu, user_input, expected_output):
    machine = pynigma.rotor.Rotor(notch, test_list, ringstu)
    assert machine.cipher(user_input) == expected_output
