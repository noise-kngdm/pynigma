import pytest
import pynigma.rotor
import pynigma.constants as constants

init_vals = [[(x, (x % constants.MAX_NUM)+1) for x in range(constants.MIN_NUM, constants.MAX_NUM+1)],
             [(x, ((x+1) % constants.MAX_NUM)+1) for x in range(constants.MIN_NUM, constants.MAX_NUM+1)]
            ]

ringstu = [1, 13, 26]
grundstu = [5, 12, 21]
notch = [2, 10, 22]

@pytest.mark.parametrize('test_list', tuple(init_vals))
@pytest.mark.parametrize('ringstu,grundstu,notch', (ringstu,grundstu,notch))
def test_rotor_init(ringstu,grundstu,notch,test_list):
    pynigma.rotor.Rotor(ringstu, grundstu,notch, test_list)