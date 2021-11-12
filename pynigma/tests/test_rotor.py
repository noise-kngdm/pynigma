import pytest
import pynigma.rotor
import pynigma.constants as constants

init_vals = [[(x, (x % constants.MAX_NUM)+1) for x in range(constants.MIN_NUM, constants.MAX_NUM+1)],
             [(x, ((x+1) % constants.MAX_NUM)+1) for x in range(constants.MIN_NUM, constants.MAX_NUM+1)]
            ]

ringstu = [2, 13]
notch = [3, 10]

@pytest.mark.parametrize('test_list', tuple(init_vals))
@pytest.mark.parametrize('ringstu,notch', (notch,ringstu))
def test_rotor_init(ringstu,notch,test_list):
    pynigma.rotor.Rotor(ringstu,notch, test_list)
