#!/usr/bin/env python3

from sys import exit
from termcolor import colored

import pynigma.constants as ct
import pynigma.common as common
from pynigma.instances import Rotors, Reflectors
from pynigma.enigma import Enigma
from pynigma.plugboard import PlugBoard


def red(string, end='\n', bold=False):
    attrs = ['bold'] if bold else []
    print(colored(string, 'red', attrs=attrs), end=end)


def magenta(string, end='\n', bold=False):
    attrs = ['bold'] if bold else []
    print(colored(string, 'magenta', attrs=attrs), end=end)


def blue(string, end='\n', bold=False):
    attrs = ['bold'] if bold else []
    print(colored(string, 'blue', attrs=attrs), end=end)


def print_banner():
    banner = """
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒  ▒   ▒▒▒   ▒▒▒   ▒   ▒   ▒▒▒▒▒▒▒▒     ▒▒▒    ▒   ▒   ▒▒▒▒▒   ▒▒▒▒
▓  ▓▓   ▓▓▓   ▓   ▓▓▓   ▓▓   ▓   ▓   ▓▓   ▓▓   ▓▓  ▓▓   ▓▓   ▓▓   ▓
▓  ▓▓▓   ▓▓▓▓    ▓▓▓▓   ▓▓   ▓   ▓  ▓▓▓   ▓▓   ▓▓  ▓▓   ▓   ▓▓▓   ▓
▓   ▓   ▓▓▓▓▓▓   ▓▓▓▓   ▓▓   ▓   ▓    ▓   ▓▓   ▓▓  ▓▓   ▓   ▓▓▓   ▓
█   █████████   ████    ██   █   █████   ██    ██  ██   ███   █
█   ████████   █████████████████████    ███████████████████████████

Python implementation of the Enigma machine.

Coded by @noise-kngdm and @LuisSS20.
Under GPL-v3.0 License.
    """
    blue(banner)


def check_and_abort(option):
    if option == 'Q':
        print("\nSee you next time!")
        exit()


def print_options(options):
    for k, v in options.items():
        print(f'{k} -> {v[1]}')


def choose_option(options, item='next item'):
    selection = None
    error = False
    while selection not in options:
        if error:
            red("The selected option is not valid.")
        print(f"Select the {item} from the following list:")
        print_options(options)
        print("Press 'Q' to abort.")

        selection = input().upper()
        check_and_abort(selection)
        if isinstance(list(options.keys())[0], int):
            try:
                selection = int(selection)
            except ValueError:
                # The user didn't choose a number
                pass

        error = True
    return options[selection][0], selection


def choose_rotors(machine):
    print('Choose the ', end='')
    red(machine, '')
    print(' rotors. Those rotors will be set from ',
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
    selected_options = options.copy()

    selected_rotors = []
    while len(selected_rotors) != machine:
        choice, option = choose_option(selected_options, 'next rotor')
        selected_rotors.append((choice, option))
        del selected_options[option]
        print()

    print("The selected rotors are, from right to left:")
    for x, y in selected_rotors:
        blue(options[y][1])
    print()

    ok = should_continue()
    print()
    if ok:
        return [x[0] for x in selected_rotors]
    else:
        return choose_rotors(machine)


def should_continue(message='Is that correct?'):
    print(f"{message}")
    answer, _ = choose_option({'Y': [True, 'Yes'], 'N': [False, 'No']},
                              'option')
    return answer


def choose_reflector(machine):
    options = {1: [Reflectors.reflector_b, 'UKW-B'],
               2: [Reflectors.reflector_c, 'UKW-C']} if machine == 3 else \
              {1: [Reflectors.reflector_b_thin, 'UKW-B thin'],
               2: [Reflectors.reflector_c_thin, 'UKW-C thin'],
               }

    reflector, choice = choose_option(options, 'reflector')
    print("The selected reflector is:")
    blue(options[choice][1], end='\n\n')
    ok = should_continue()
    print()
    if ok:
        return reflector
    else:
        return choose_reflector(machine)


def rotors_configuration_ok(conf, machine):
    for x in conf:
        if x < ct.MIN_CHAR or x > ct.MAX_CHAR:
            return False
    return len(conf) == machine


def choose_characters(machine, text):
    print(f'Introduce a string of characters with the desired {text}.')
    print('Bear in mind that they will be set in the machine ', end='')
    blue('from right to left.', bold=True)
    configuration = input().upper()
    while not rotors_configuration_ok(configuration, machine):
        red(f'Set a proper {text} configuration')
        configuration = input().upper()

    print(f'The selected {text} from right to left is: ', end='')
    blue(f'{configuration}\n')

    if should_continue():
        print()
        return configuration
    else:
        return choose_characters(machine, text)


def choose_plugboard():
    print('Introduce a string of up to 10 pairs of characters space-separated '
          'to represent the different plugboard patches.')
    plugboard = input().upper()
    patches = [x for x in plugboard.split() if x]

    if not (all([*map(lambda x: x >= ct.MIN_CHAR and x <= ct.MAX_CHAR,
                      ''.join(patches))])):
        red('The string must be composed of letters only.\n')
        return choose_plugboard()

    if not (all([*map(lambda x: len(x) == 2, patches)])):
        red('The string must be composed of character', end='')
        red('pairs.\n', bold=True)

        return choose_plugboard()

    try:
        ret = PlugBoard([(common.char_to_int(x[0]), common.char_to_int(x[1]))
                         for x in patches])
    except (ValueError, TypeError) as e:
        red(f"There was an error while creating the Plugboard: {e}")
        return choose_plugboard()
    else:
        print()
        return ret


def set_machine():
    options_machine = {3: [3, 'M3, Wehrmacht'], 4: [4, 'M4, Kriegsmarine']}
    machine, _ = choose_option(options_machine, item='machine')
    rotors = choose_rotors(machine)
    reflector = choose_reflector(machine)
    ringstellung = [common.char_to_int(x) for
                    x in choose_characters(machine, 'ringstellung')]
    grundstellung = [common.char_to_int(x) for
                     x in choose_characters(machine, 'grundstellung')]
    plugboard = choose_plugboard()

    reflector = reflector()
    rotors = [x() for x in rotors]
    for i in range(len(ringstellung)):
        rotors[i].ringstellung = ringstellung[i]

    return Enigma(rotors=rotors, positions=grundstellung, reflector=reflector,
                  plugboard=plugboard), machine


def cipher(enigma_machine):
    text = input("Introduce the text that you want to cipher/decipher: ")
    if should_continue('Does the text contains redundant information at'
                       ' the beggining and end? If so, it will be '
                       'removed.'):
        text = text[8:-8]

    ciphertext = enigma_machine.cipher(text)
    ciphertext = [ciphertext[i:i+4] for i in range(0, len(ciphertext), 4)]

    print("The ciphered text is: ")
    magenta(f"{' '.join(ciphertext)}")


def change_grundstellung(machine):
    if should_continue('Do you want to change the grundstellung?'):
        return [common.char_to_int(x) for
                x in choose_characters(machine, 'grundstellung')]
    return None


def main():
    print_banner()
    enigma, machine = set_machine()
    while True:
        cipher(enigma)

        if should_continue('Do you want to finish the program?'):
            break

        if grundstellung := change_grundstellung(machine):
            enigma.change_grundstellung(grundstellung)

    magenta('See you soon!!\n', bold=True)


if __name__ == '__main__':
    main()
