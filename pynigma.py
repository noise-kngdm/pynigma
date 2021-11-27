#!/usr/bin/env python3

from sys import exit
from termcolor import colored
from pynigma.instances import Rotors, Reflectors


def red(string, end='\n', bold=False):
    attrs = ['bold'] if bold else []
    print(colored(string, 'red', attrs=attrs), end=end)


def blue(string, end='\n', bold=False):
    attrs = ['bold'] if bold else []
    print(colored(string, 'blue', attrs=attrs), end=end)


def print_banner():
    banner = """                      __                        
______ ____ __  ____ |__|  ____   _____ _____   
\____ \\   |  |/    \|  | / ___\ /     \\__  \  
|  |_\ \\___  |   |  \  |/ /_/  \  | |  \/ __ \_
|   ___// ____|___|  /__|\___  /|__|_|  /____  /
|__|    \/         \/   /_____/       \/     \/ 

------------------------------------------------

Python implementation of the Enigma machine.

Coded by @noise-kngdm and @LuisSS20.
Under GPL-v3.0 License.
    """
    blue(banner)


def check_and_abort(option):
    if option == 'Q':
        print("\nSee you next time!")
        exit()


def choose_machine():
    options_str = "Which machine would you like to use? The available options"\
                  " are [M3, M4]. Press 'Q' to abort: "

    options = {'M3', 'M4', '3', '4', 'Q'}
    while (machine := input(options_str).upper()) not in options:
        print("Choose a valid option")
    check_and_abort(machine)

    return int(machine[-1])

    
def choose_rotors(machine):
    def print_options():
        for k, v in options.items():
            print(f'{k} -> {v[1]}')

    print('Choose ', end='')
    red(machine, '')
    print(' rotors from the following list. Those rotors will be set from ',
          end='')
    blue('right to left', end='', bold=True)
    print(' in the machine.\n')

    options = {1: [Rotors.rotor_i, 'Rotor I'],
               2: [Rotors.rotor_ii, 'Rotor II'],
               3: [Rotors.rotor_iii, 'Rotor III'],
               4: [Rotors.rotor_iv, 'Rotor IV'],
               5: [Rotors.rotor_v, 'Rotor V'],
               6: [Rotors.rotor_vi, 'Rotor VI'],
               7: [Rotors.rotor_vii, 'Rotor VII'],
               8: [Rotors.rotor_viii, 'Rotor VIII']
               }
    m4_options = {9:  [Rotors.rotor_beta, 'Rotor BETA'],
                  10: [Rotors.rotor_gamma, 'Rotor GAMMA']}

    if machine == 4:
        options.update(m4_options)

    print_options()


def main():
    print_banner()
    machine = choose_machine()
    rotors = choose_rotors(machine)


if __name__ == '__main__':
    main()
