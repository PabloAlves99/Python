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

        if text in '=':
            self._connect_button_clicked(
                _button, self._eq)

        if text == 'C':
            _button.clicked.connect(self.clear_display_and_info)

        if text == 'CE':
            _button.clicked.connect(self.display.clear)

        if text in '+-*/%½^√':
            self._connect_button_clicked(
                _button, self._make_slot(self._operator_clicked, _button))

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

    def reverse_number(self, text):
        return float(text) * -1

    def root_square(self):
        try:
            number = float(self._left)
            if number < 0:
                raise ValueError(
                    "A raiz quadrada de um número negativo não é definida.")
            return math.sqrt(number)
        except ValueError as e:
            return f"Erro: {e}"
        except OverflowError as e:
            return f"Erro: {e}"

    def calculate_power(self, base, exponent):
        return float(base) ** exponent

    def calculate_half(self, text):
        return 0.5 * float(text)

    def calculate_percentage(self, number, percentage):
        return (float(percentage) / 100) * float(number)

    def _get_display_text_stripped(self):
        return self.display.text().strip()

    def perform_custom_operation(self):

        if self._special_op == '√':
            # self._left = float(self.root_square())
            ...

    def perform_basic_calculation(self):
        self.equation = f'{self._left} {self._op} {self._right}'

        if self._op == '+':
            self._left = float(self._left) + float(self._right)
        elif self._op == '-':
            self._left = float(self._left) - float(self._right)
        elif self._op == '*':
            self._left = float(self._left) * float(self._right)
        elif self._op == '/':
            try:
                self._left = float(self._left) / float(self._right)
            except ZeroDivisionError:
                print('Zero Division Error')

        print(f'Resultado = {self._left}')
        self.info.setText(f'{self.info.text()} = {self._left}')

    def _operator_clicked(self, _button):
        text = _button.text()

        if self._get_display_text_stripped():
            if self._left is None:
                self._left = float(self.display.text())
                self.equation = f'{self._left} {text} '
            else:
                self._right = float(self.display.text())
                self.perform_basic_calculation()

        self._op = text
        print(f'Operação = {self._op}')
        self.display.clear()

    # Criar uma lógica para calculo especial
    # Se _special_op is not None o calcula todo seguinte é feito dentro do
    # calculo especial, que após um gatilho dará o calculo final.
    # Alguns calculos especiais precisam de números seguintes para funcionar
    def _eq(self):
        text = self.display.text()

        if self.is_valid_number(text):
            self._right = float(text)

        if self._left:
            self.perform_basic_calculation()

        self.display.clear()
