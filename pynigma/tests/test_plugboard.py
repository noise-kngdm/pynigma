import pytest
import pynigma.plugboard


@pytest.mark.parametrize('test_list', [[(x, x) for x in range(1, 10)],
                                       [],
                                       [(1, 2), (3, 4), (3, 3)]
                                       ])
def test_plugboard_init(test_list):
    pynigma.plugboard.PlugBoard(test_list)
