#!/usr/bin/env python3

from sys import exit
from termcolor import colored

import pynigma.constants as ct
import pynigma.common as common
from pynigma.instances import Rotors, Reflectors
from pynigma.enigma import Enigma
from pynigma.plugboard import PlugBoard


def red(string, end='\n', bold=False):
    """
    Prints a string in red using termcolor.

    Parameters
    ----------
    string : str
        The string that will be printed.
    end : str
        The characters sequence that will be written after the string.
    bold : bool
        If the string should be printed using a bold style or not.
    """
    attrs = ['bold'] if bold else []
    print(colored(string, 'red', attrs=attrs), end=end)


def magenta(string, end='\n', bold=False):
    """
    Prints a string in magenta using termcolor.

    Parameters
    ----------
    string : str
        The string that will be printed.
    end : str
        The characters sequence that will be written after the string.
    bold : bool
        If the string should be printed using a bold style or not.
    """
    attrs = ['bold'] if bold else []
    print(colored(string, 'magenta', attrs=attrs), end=end)


def blue(string, end='\n', bold=False):
    """
    Prints a string in blue using termcolor.

    Parameters
    ----------
    string : str
        The string that will be printed.
    end : str
        The characters sequence that will be written after the string.
    bold : bool
        If the string should be printed using a bold style or not.
    """
    attrs = ['bold'] if bold else []
    print(colored(string, 'blue', attrs=attrs), end=end)


def print_banner():
    """
    Print a banner with information about the program.
    """
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
    """
    Exit the program if needed.

    Parameters
    ----------
    options : str
        The option that will be checked. If its value is 'Q', the
        program will end its execution.
    """
    if option == 'Q':
        print("\nSee you next time!")
        exit()


def print_options(options):
    """
    Print the different items on a dictionary.

    Parameters
    ----------
    options : dict
        The dictionary that will be printed.
    """
    for k, v in options.items():
        print(f'{k} -> {v[1]}')


def choose_option(options, item='next item'):
    """
    Return a option chosen by an user after showing a parametrized dialog.

    Parameters
    ----------
    options : dict
        A dictionary that contains what the user should write as key, and, as
        value, a list with the object chosen in the first position and its
        description in the second one.
    item : str
        String that describes what the user is choosing.

    Returns
    -------
        The object chosen by the user.
    """
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
    """
    Return the rotors chosen by the user.

    Parameters
    ----------
    machine : int
        The number of rotors of the machine.

    Returns
    -------
    list of function
        A list with functions that returns the requested Rotors.
    """
    print('Choose the ', end='')
    red(machine, '')
    print(' rotors. Those rotors will be set from ',
          end='')
    blue('left to right', end='', bold=True)
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

    selected_options = options.copy()
    selected_rotors = []
    if machine == 4:
        options.update(m4_options)
        choice, option = choose_option(m4_options, 'next rotor')
        selected_rotors.append((choice, option))

    while len(selected_rotors) != machine:
        choice, option = choose_option(selected_options, 'next rotor')
        selected_rotors.append((choice, option))
        del selected_options[option]
        print()

    print("The selected rotors are, from left to right:")
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
    """
    Print a Y/N question and return a boolean depending on the answer.

    Parameters
    ----------
    message : str
        Custom message that will be printed.

    Returns
    -------
    bool
        True if 'Y' was chosen, False otherwise.
    """
    print(f"{message}")
    answer, _ = choose_option({'Y': [True, 'Yes'], 'N': [False, 'No']},
                              'option')
    return answer


def choose_reflector(machine):
    """
    Return the reflector chosen by the user.

    Parameters
    ----------
    machine : int
        The number of rotors of the machine.

    Returns
    -------
    function
        Function that returns the chosen reflector.
    """
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
    """
    Check that a configuration string has the expected format.

    Parameters
    ----------
    conf : str
        Configuration string that will be checked.
    machine : int
        Machine's number of rotors. 
    """
    for x in conf:
        if x < ct.MIN_CHAR or x > ct.MAX_CHAR:
            return False
    return len(conf) == machine


def choose_characters(machine, text):
    """
    Return a string containing Enigma configuration parameters.

    It should be used to get the ringstellung or the grundstellung to
    later create a Enigma instance. It uses the machine version to
    compute the total lenght that the return value should had.

    Parameters
    ----------
    machine : int
        The machine version that is required, either 3 or 4.
    text : str
        The text that should be printed to indicate which parameter
        the user is configuring.

    Returns
    -------
    str
        The configuration introduced by the user.
    """
    print(f'Introduce a string of characters with the desired {text}.')
    print('Bear in mind that they will be set in the machine ', end='')
    blue('from left to right.', bold=True)
    configuration = input().upper()
    while not rotors_configuration_ok(configuration, machine):
        red(f'Set a proper {text} configuration')
        configuration = input().upper()

    print(f'The selected {text} from left to right is: ', end='')
    blue(f'{configuration}\n')

    if should_continue():
        print()
        return configuration
    else:
        return choose_characters(machine, text)


def choose_plugboard():
    """
    Return a PlugBoard to use with the Enigma machine.

    Returns
    -------
    PlugBoard
        The PlugBoard as it was configured by the user.
    """
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
        print('The selected plugboard is: ', end='')
        blue(f'{plugboard}')
        if should_continue():
            print()
            return ret
        else:
            return choose_plugboard()


def set_machine():
    """
    Return a Enigma machine configured with the user requirements.

    Returns
    -------
    Enigma
        The enigma machine configured by the user.
    """
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
    """
    Cipher the text introduced by an user and return its output properly
    formated.

    Parameters
    ----------
    enigma_machine : Enigma
        The enigma machine that will be used to cipher the text.
    """
    text = input("Introduce the text that you want to cipher/decipher: ")
    if should_continue('\nDoes the text contains redundant information at'
                       ' the beggining and end? If so, it will be '
                       'removed.'):
        text = ''.join(text.split())[8:-8]
    print()

    ciphertext = enigma_machine.cipher(text)
    ciphertext = [ciphertext[i:i+4] for i in range(0, len(ciphertext), 4)]

    print("The ciphered text is: ")
    magenta(f"{' '.join(ciphertext)}\n")


def change_grundstellung(machine):
    """
    Return the new grundstellung set by the user.

    Parameters
    ----------
    machine : int
        Enigma machine model that's being used.

    Returns
    -------
    list of int
        The new grundstellung settings for the machine.
    """
    if should_continue('Do you want to change the grundstellung?'):
        return [common.char_to_int(x) for
                x in choose_characters(machine, 'grundstellung')]
    return None


def main():
    """Main method."""
    print_banner()
    enigma, machine = set_machine()
    while True:
        cipher(enigma)

        if should_continue('Do you want to finish the program?'):
            break

        if grundstellung := change_grundstellung(machine):
            enigma.grundstellung = grundstellung

    magenta('See you soon!!\n', bold=True)


if __name__ == '__main__':
    main()
