#  pylint: disable=missing-docstring
#  pylint: disable=no-name-in-module
#  type: ignore
import math
import re
from PySide6.QtWidgets import QGridLayout
from PySide6.QtCore import Slot
from main import Info, Display, Button, MainWindow

NUM_REGEX = re.compile(r'^[0-9]$')


class ButtonsGrid(QGridLayout):
    def __init__(
            self, _display: Display, _info: Info, window: MainWindow,
            *args, **kwargs) -> None:
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
        self.window = window
        self._left = None
        self._right = None
        self._op = None
        self.setSpacing(3)
        self._equation = ''
        self.create_buttons()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def create_buttons(self):
        self.display.eq_pressed.connect(self._eq)
        self.display.del_pressed.connect(self.display.backspace)
        self.display.clear_pressed.connect(self.clear_display_and_info)
        self.display.input_pressed.connect(self.insert_text_display)
        self.display.operator_pressed.connect(self._operator_clicked)

        for row_number, row in enumerate(self._grid_mask):
            for column, text_grid in enumerate(row):
                _button = Button(text_grid)

                if not self.is_num(text_grid):

                    self._config_special_button(_button)

                    if _button.text() == '=':
                        _button.setProperty("cssClass", "specialButtonSpace")
                    else:
                        _button.setProperty("cssClass", "specialButton")

                self.addWidget(_button, row_number, column)

                slot = self._make_slot(
                    self.insert_text_display, text_grid)

                self._connect_button_clicked(_button, slot)

    def _connect_button_clicked(self, button, slot):
        button.clicked.connect(slot)
        self.display.setFocus()

    @Slot()
    def _make_slot(self, func, *args, **kwargs):
        @Slot()
        def real_slot():
            func(*args, **kwargs)
            self.display.setFocus()
        return real_slot

    def insert_text_display(self, text):

        new_display_text = self.display.text() + text

        if not self.is_valid_number(new_display_text):
            return

        self.display.insert(text)
        self.display.setFocus()

    def _config_special_button(self, _button):
        text = _button.text()

        if text == '=':
            self._connect_button_clicked(
                _button, self._eq)

        if text == '←':
            self._connect_button_clicked(_button, self.remove_last_character)

        if text == 'C':
            _button.clicked.connect(self.clear_display_and_info)

        if text == 'CE':
            _button.clicked.connect(self.display.clear)

        if text == '±':
            _button.clicked.connect(self.reverse_number)

        if text == '½':
            _button.clicked.connect(self.calculate_half)

        if text == '√':
            _button.clicked.connect(self.root_square)

        if text in '+-*/%^':
            self._connect_button_clicked(
                _button, self._make_slot(
                    self._operator_clicked, _button.text()))

        self.display.setFocus()

    @Slot()
    def clear_display_and_info(self):
        self.display.clear()
        self.info.clear()
        self._op = None
        self._left = None
        self._right = None
        self.display.setFocus()

    @Slot()
    def is_num(self, string: str):
        return bool(NUM_REGEX.search(string))

    @Slot()
    def is_valid_number(self, string: str):
        valid = False
        try:
            float(string)
            valid = True
        except ValueError:
            valid = False
        return valid

    @Slot()
    def remove_last_character(self):
        if self._get_display_text_stripped():
            new_display = self.display.text()
            self.display.setText(new_display[:-1])
            self.display.setFocus()

    @Slot()
    def _get_display_text_stripped(self):
        return self.display.text().strip()

    def handle_error(self, error_message):
        msg_box = self.window.make_msg_box()
        msg_box.setText(error_message)
        msg_box.setIcon(msg_box.Icon.Critical)
        msg_box.setWindowTitle('ERROR: -> Pablo Alves - Calculator')
        msg_box.exec()
        self.display.setFocus()

    @Slot()
    def _operator_clicked(self, text):

        if self._get_display_text_stripped():

            if self._left is None:

                if self._op is None:
                    self._left = round(float(self.display.text()), 3)

                elif self._op == '-':
                    self._left = round(
                        float(f'{self._op}{self.display.text()}'), 3)

                else:
                    self._left = round(float(self.display.text()), 3)

            else:
                self._right = round(float(self.display.text()), 3)
                self.perform_operations()

        if self._left is not None:
            self.equation = f'{self._left} {text} '

        self._op = text
        self.display.clear()
        self.display.setFocus()

    @Slot()
    def _eq(self):
        text = self.display.text()

        if self.is_valid_number(text):

            if self.handle_large_result(text):
                return

            if self._left is not None:
                self._right = round(float(text), 3)
            else:
                self._left = round(float(text), 3)
                self.display.clear()
                self.equation = f'{self._left} '
                return

        try:
            if self._op is not None and self._right is not None:
                self.perform_operations()

        except (ValueError, TypeError):
            self.handle_error(
                "Entrada inválida. Insira um número válido.")

        self.display.clear()
        self.display.setFocus()

    @Slot()
    def perform_operations(self):

        self.equation = f'{self._left} {self._op} {self._right}'

        button_functions = {
            '+': self.perform_addition,
            '-': self.perform_subtraction,
            '*': self.perform_multiplication,
            '/': self.perform_division,
            '^': self.calculate_power,
            '%': self.calculate_percentage,
        }
        if self._op in button_functions:
            try:
                number = round(float(button_functions[self._op]()), 3)
                if not self.handle_large_result(number):
                    self._left = number
                else:
                    return

            except ZeroDivisionError:
                self.handle_error('Zero Division Error')
                self._left = None
            except OverflowError:
                self.handle_error('Essa conta não pode ser realizada.')
                self._left = None
            except (TypeError, ValueError):
                self.handle_error(
                    'Erro de tipo. Verifique os valores inseridos.')
                self._left = None

        self.info.setText(f'{self.info.text()} = {self._left}')
        self.display.setFocus()

    @Slot()
    def calculate_percentage(self):
        return round((self._left / 100) * self._right, 3)

    @Slot()
    def perform_addition(self):
        return round(self._left + self._right, 3)

    @Slot()
    def perform_subtraction(self):
        return round(self._left - self._right, 3)

    @Slot()
    def perform_multiplication(self):
        return round(self._left * self._right, 3)

    @Slot()
    def perform_division(self):
        return round(self._left / self._right, 3)

    @Slot()
    def root_square(self):
        try:
            number = float(self.display.text())

            if self.is_valid_number(number):

                if number < 0:
                    self.handle_error(
                        "A raiz quadrada de número negativo não é definida.")

                result = round(math.sqrt(number), 3)
                equation_text = f'√({self.display.text()})'

                if self._left is not None:

                    if self._right is None:
                        self.equation += equation_text
                    else:
                        self.equation = (
                            f'{self._left} {self._op} {equation_text}')

                else:
                    self.equation = equation_text

                self.display.setText(str(result))

        except (TypeError, ValueError):
            self.handle_error(
                'Erro de tipo. Verifique os valores inseridos.')

    @Slot()
    def reverse_number(self):

        try:
            number = float(self.display.text())

            if self.is_valid_number(number):
                self.display.setText(str(round(number * -1, 3)))

        except (TypeError, ValueError):
            self.handle_error(
                'Erro de tipo. Verifique os valores inseridos.')

    @Slot()
    def calculate_half(self):

        try:
            number = float(self.display.text())

            if self.is_valid_number(number):
                self.display.setText(str(round(0.5 * number, 3)))

        except (TypeError, ValueError):
            self.handle_error(
                'Erro de tipo. Verifique os valores inseridos.')

    @Slot()
    def calculate_power(self):
        return round(self._left ** self._right, 3)

    def handle_large_result(self, result):
        """
        Exibe um erro se o resultado for maior que um limite específico.
        """
        limit = 1e15  # Defina o limite conforme necessário

        if float(result) > limit:
            error_message = (
                f"O resultado é muito grande para ser exibido.\n"
                f"O resultado é {result:.15f}...")
            self.handle_error(error_message)
            return True

        return False
