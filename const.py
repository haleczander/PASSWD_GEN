PROGRAM_NAME = "Password generator"
DEFAULT_LENGTH = 12
DEFAULT_LOWER_CASE = False
DEFAULT_UPPER_CASE = False
DEFAULT_NUMBERS = False
DEFAULT_SYMBOLS = False
DEFAULT_SYMBOLS_LIST = "!@#$%^&*()-_=+[]{};:,.<>?"

HELP_LENGTH = "Password length"
HELP_UPPER_CASE = "Include uppercase letters (A-Z)"
HELP_LOWER_CASE = "Include lowercase letters (a-z)"
HELP_NUMBERS = "Include numbers (0-9)"
HELP_SYMBOLS = "Include symbols (e.g. !@#$%%^&*)"
HELP_SYMBOLS_LIST = f"Custom list of accepted symbols"

from string import ascii_lowercase, ascii_uppercase, digits
from charset import CharSet

ARGS_CHARSET_CONFIG = {
    'lowercase': (CharSet(ascii_lowercase), DEFAULT_LOWER_CASE, HELP_LOWER_CASE),
    'uppercase': (CharSet(ascii_uppercase), DEFAULT_UPPER_CASE, HELP_UPPER_CASE),
    'numbers':   (CharSet(digits), DEFAULT_NUMBERS, HELP_NUMBERS),
    'symbols':   (None, DEFAULT_SYMBOLS, HELP_SYMBOLS),
}