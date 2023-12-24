#  pylint: disable=missing-docstring
#  pylint: disable=no-name-in-module
#  type: ignore
import math
import re
from PySide6.QtWidgets import QGridLayout
from PySide6.QtCore import Slot
from main import Info, Display, Button

NUM_OR_DOT_REGEX = re.compile(r'^[0-9]$')


class ButtonsGrid(QGridLayout):
    def __init__(
            self, _display: Display, _info: Info, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._grid_mask = [
            ['%', 'CE', 'C', '←'],
            ['½', '^', '√', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['±', '0', '.', '='],
        ]
        self.display = _display
        self.info = _info
        self._left = None
        self._right = None
        self._op = None
        self._special_op = None
        self.setSpacing(3)
        self._equation = ''
        self.create_buttons()

    @property
    def equation(self):
        return self.equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def create_buttons(self):
        for i, row in enumerate(self._grid_mask):
            for column, text_grid in enumerate(row):
                _button = Button(text_grid)

                if not self.is_num_or_dot(text_grid):
                    self._config_special_button(_button)
                    if _button.text() == '=':
                        _button.setProperty("cssClass", "specialButton")

                self.addWidget(_button, i, column)
                slot = self._make_slot(self.insert_text_display, _button)
                self._connect_button_clicked(_button, slot)

    def clear_display_and_info(self):
        self.display.clear()
        self.info.clear()
        self._op = None
        self._special_op = None
        self._left = None
        self._right = None

    def _connect_button_clicked(self, button, slot):
        button.clicked.connect(slot)

    def _config_special_button(self, _button):
        text = _button.text()

        if text == '=':
            self._connect_button_clicked(
                _button, self._eq)

        if text == 'C':
            _button.clicked.connect(self.clear_display_and_info)

        if text == 'CE':
            _button.clicked.connect(self.display.clear)

        if text in '+-*/%½^√±':
            self._connect_button_clicked(
                _button, self._make_slot(self._operator_clicked, _button))

        if text == '←':
            self._connect_button_clicked(_button, self.remove_last_character)

    def _make_slot(self, func, *args, **kwargs):
        @Slot()
        def real_slot():
            func(*args, **kwargs)
        return real_slot

    @Slot()
    def insert_text_display(self, _button):

        text = _button.text()
        new_display_text = self.display.text() + text

        if not self.is_valid_number(new_display_text):
            return

        self.display.insert(text)
        self.display.setFocus()

    def is_num_or_dot(self, string: str):
        return bool(NUM_OR_DOT_REGEX.search(string))

    def is_valid_number(self, string: str):
        valid = False
        try:
            float(string)
            valid = True
        except ValueError:
            valid = False
        return valid

    def display_special_calculation(self, result):
        equation_text = f'{self._op}({self._left}) = {result}'
        self.equation = equation_text
        self._right = None

    def special_calculation(self, text):
        if text == '√':
            self._op = text
            self._left = self.root_square()
            self.display.clear()

        elif text == '½':
            self._op = text
            self._left = self.calculate_half()
            self.display.clear()

        elif text == '±':
            self._op = text
            self.reverse_number()
            self.display.clear()

    def remove_last_character(self):
        if self._get_display_text_stripped():
            new_display = self.display.text()
            self.display.setText(new_display[:-1])

    def reverse_number(self):
        result = self._left * -1
        self._left = result
        self.equation = str(result)
        self._right = None
        return result

    def root_square(self):
        if self._left is not None:
            number = float(self._left)
        else:
            number = 0

        if number < 0:
            raise ValueError(
                "A raiz quadrada de um número negativo não é definida.")

        result = math.sqrt(number)
        self.display_special_calculation(result)
        return result

    def calculate_power(self):
        return self._left ** self._right

    def calculate_half(self):
        result = 0.5 * self._left
        self.display_special_calculation(result)
        return result

    def calculate_percentage(self):
        return (self._left / 100) * self._right

    def perform_addition(self):
        return self._left + self._right

    def perform_subtraction(self):
        return self._left - self._right

    def perform_multiplication(self):
        return self._left * self._right

    def perform_division(self):
        return self._left / self._right

    def perform_operations(self):
        if self._right is None:
            self._right = 0

        self.equation = f'{self._left} {self._op} {self._right}'

        button_functions = {
            '+': self.perform_addition,
            '-': self.perform_subtraction,
            '*': self.perform_multiplication,
            '/': self.perform_division,
            '^': self.calculate_power,
            '√': self.root_square,
            '½': self.calculate_half,
            '%': self.calculate_percentage,
            '±': self.reverse_number,
        }
        if self._op in button_functions:
            try:
                self._left = float(button_functions[self._op]())

            except ZeroDivisionError:
                print('Zero Division Error')
                self._left = None
            except OverflowError:
                print('Essa conta não pode ser realizada.')
                self._left = None
            except (TypeError, ValueError):
                self.handle_exception(
                    'Erro de tipo. Verifique os valores inseridos.')
                self._left = None

        print(f'Resultado = {self._left}')

        if self._op in '√½±':
            return

        self.info.setText(f'{self.info.text()} = {self._left}')

    def _get_display_text_stripped(self):
        return self.display.text().strip()

    def _operator_clicked(self, _button):
        text = _button.text()

        if self._get_display_text_stripped():

            if self._left is None:
                self._left = float(self.display.text())
                if text in '√½±':
                    self.special_calculation(text)
                    return
            else:
                self._right = float(self.display.text())
                self.perform_operations()

        if self._left is not None:
            self.equation = f'{self._left} {text} '

        self._op = text
        print(f'Operação = {self._op}')
        self.display.clear()

    def _eq(self):
        text = self.display.text()

        if self.is_valid_number(text):
            self._right = float(text)

        try:
            if self._left:
                self.perform_operations()
            else:
                self._left = float(text)
                self.equation = f'{self._left} '
                if self._op in '√½±':
                    self.special_calculation(text)

        except ValueError:
            self.handle_exception(
                "Entrada inválida. Insira um número válido.")
            self._left = None

        self.display.clear()

    def handle_exception(self, error_message):
        # Método para exibir mensagens de erro ao usuário.
        print(f"Erro: {error_message}")
