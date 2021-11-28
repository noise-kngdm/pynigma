# Pynigma
Python implementation of the enigma machine.

## Install
To install `Pynigma`, clone the repository.
```zsh
git clone https://github.com/noise-kngdm/pynigma.git
```  

### Install the dependencies
It's required a Python version equal or greater than `3.9`.
#### Install Poetry (required)

First it's necessary to install Poetry, the dependency manager of the project, which ensures that the project is running on an environment with all the required dependencies.

To install Poetry in a Linux system, run the following command [as told by the Poetry installation manual](https://python-poetry.org/docs/master/#installation):
```zsh
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```  

#### Install the rest of the dependencies
```zsh
cd pynigma;
poetry install;
```  


## Usage
To use the project, first activate the virtual environment with all the dependencies using Poetry:
```zsh
poetry shell
```

Then, execute the `pynigma.py` file to have access to an interactive Enigma machine. The program is self-describing and has colored output to help understanding how it works.  

```
➜  pynigma git:(feature/24-enhance-readme) ✗ ./pynigma.py

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
    
Select the machine from the following list:
3 -> M3, Wehrmacht
4 -> M4, Kriegsmarine
Press 'Q' to abort.
3
Choose the 3 rotors. Those rotors will be set from left to right in the machine.

Select the next rotor from the following list:
1 -> Rotor I
2 -> Rotor II
3 -> Rotor III
4 -> Rotor IV
5 -> Rotor V
6 -> Rotor VI
7 -> Rotor VII
8 -> Rotor VIII
Press 'Q' to abort.
```
