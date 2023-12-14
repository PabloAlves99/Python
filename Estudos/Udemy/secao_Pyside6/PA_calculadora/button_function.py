#  pylint: disable=missing-docstring
#  pylint: disable=no-name-in-module
#  type: ignore
import math
import re
# self._grid_mask = [
#     ['%', 'CE', 'C', '←'],
#     ['½', '^', '√', '/'],
#     ['7', '8', '9', '*'],
#     ['4', '5', '6', '-'],
#     ['1', '2', '3', '+'],
#     ['±', '0', '.', '='],
# ]

NUM_OR_DOT_REGEX = re.compile(r'^[0-9]$')


def is_num_or_dot(string: str):
    return bool(NUM_OR_DOT_REGEX.search(string))


def is_valid_number(string: str):
    valid = False
    try:
        float(string)
        valid = True
    except ValueError:
        valid = False
    return valid


def reverse_number(text):
    return float(text) * -1


def root_square(text):
    try:
        number = float(text)
        if number < 0:
            raise ValueError(
                "A raiz quadrada de um número negativo não é definida.")
        return math.sqrt(number)
    except ValueError as e:
        return f"Erro: {e}"
    except OverflowError as e:
        return f"Erro: {e}"


def calculate_power(base, exponent):
    return float(base) ** exponent


def calculate_half(text):
    return 0.5 * float(text)


def calculate_percentage(number, percentage):
    return (float(percentage) / 100) * float(number)
