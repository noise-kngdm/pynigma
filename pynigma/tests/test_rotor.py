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


@pytest.mark.parametrize('test_list', tuple(init_vals))
@pytest.mark.parametrize('ringstu', ringstellung)
@pytest.mark.parametrize('notch', (notch,))
def test_rotor_init(notch, test_list, ringstu):
    pynigma.rotor.Rotor(notch, test_list, ringstu)


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
