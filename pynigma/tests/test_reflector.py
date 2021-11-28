import pytest
from pynigma.reflector import Reflector
import pynigma.constants as constants

init_vals = [
    [(x, (x+1) % constants.NUM_CHARS) for x in range(constants.MIN_NUM,
                                                     constants.NUM_CHARS)],

    [(3, 23), (8, 5), (4, 10), (18, 8), (10, 1), (11, 20), (17, 21), (13, 0),
     (23, 7), (0, 18), (24, 13), (6, 3), (5, 25), (7, 22), (20, 11), (16, 9),
     (2, 14), (22, 16), (14, 17), (9, 15), (15, 2), (19, 6), (21, 19),
     (25, 24), (12, 12), (1, 4)],

    [(16, 12), (4, 9), (17, 24), (11, 3), (10, 16), (5, 20), (0, 6), (2, 25),
     (20, 7), (7, 19), (23, 0), (15, 13), (21, 8), (24, 18), (1, 21),
     (22, 14), (8, 1), (25, 23), (13, 11), (3, 22), (18, 17), (6, 10), (14, 2),
     (9, 15), (19, 5), (12, 4)]
]


@pytest.mark.parametrize('test_values', tuple(init_vals))
def test_reflector_init(test_values):
    Reflector(test_values)


wrong_values = [[(3, 23), (8, 5), (4, 5), (18, 8), (10, 1), (11, 20), (17, 21),
                (13, 0), (23, 7), (0, 18), (24, 13), (6, 3), (5, 25), (7, 22),
                (20, 11), (16, 9), (2, 14), (22, 16), (14, 17), (9, 15),
                (15, 2), (19, 6), (21, 19), (25, 24), (12, 12), (1, 4)],

                [(3, 23), (3, 5), (4, 10), (18, 8), (10, 1), (11, 20),
                 (17, 21), (13, 0), (23, 7), (0, 18), (24, 13), (6, 3),
                 (5, 25), (7, 22), (20, 11), (16, 9), (2, 14), (22, 16),
                 (14, 17), (9, 15), (15, 2), (19, 6), (21, 19), (25, 24),
                 (12, 12), (1, 4)]
                ]


@pytest.mark.parametrize('test_values', tuple(wrong_values))
def test_reflector_init_ko(test_values):
    with pytest.raises(Exception):
        Reflector(test_values)
