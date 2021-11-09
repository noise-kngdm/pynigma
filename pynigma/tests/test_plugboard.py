import pytest
import pynigma.plugboard

init_vals = [[(x, x + 10) for x in range(1, 10)],
             [],
             [(1, 2), (3, 4), (5, 6)]
             ]


@pytest.mark.parametrize('test_list', tuple(init_vals))
def test_plugboard_init(test_list):
    pynigma.plugboard.PlugBoard(test_list)


@pytest.mark.parametrize('init_params,user_input,expected_output',
                         [(init_vals[0], 1, 11),
                          (init_vals[0], 2, 12),
                          (init_vals[0], 3, 13),
                          (init_vals[0], 4, 14),
                          (init_vals[0], 14, 4),
                          (init_vals[0], 20, 20),
                          (init_vals[1], 4, 4),
                          (init_vals[1], 13, 13),
                          (init_vals[1], 20, 20),
                          (init_vals[2], 3, 4),
                          (init_vals[2], 4, 3),
                          (init_vals[2], 8, 8),
                          (init_vals[2], 9, 9),
                          ])
def test_plugboard_cipher(init_params, user_input, expected_output):
    machine = pynigma.plugboard.PlugBoard(init_params)
    assert machine.cipher(user_input) == expected_output


@pytest.mark.parametrize('init_params',
                         [[(5, 5)],
                          [(1, 2),
                           (3, 4),
                           (5, 6),
                           (7, 8),
                           (9, 10),
                           (11, 12),
                           (13, 14),
                           (15, 16),
                           (17, 18),
                           (19, 20),
                           (20, 21),
                           (22, 23)
                           ],
                          [(3, 4),
                           (4, 5)],
                          [(4, 4)]])
def test_plugboard_init_ko(init_params):
    with pytest.raises(Exception):
        pynigma.plugboard.Plugboard(init_params)
