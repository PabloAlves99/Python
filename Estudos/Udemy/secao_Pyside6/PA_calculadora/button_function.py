
#  pylint: disable=no-name-in-module
#  type: ignore

"""
Módulo com funções relacionadas aos botões da calculadora.

Este módulo define a classe `ButtonsGrid`, que herda de `QGridLayout` e
gerencia a disposição e funcionalidade dos botões em uma calculadora.
As funções específicas associadas aos diferentes tipos de botões são
usadas para realizar operações quando os botões são pressionados.

Módulo: button_function.py
Autor: Pablo Alves

Classes:
    ButtonsGrid: Uma classe que herda de QGridLayout e define a disposição e
    funcionalidade dos botões em uma calculadora.

Módulo dependente:
    main: Módulo contendo as definições para Info, Display, Button e MainWindow
    que são usados pela classe ButtonsGrid.

Funções:

    - perform_addition(): Executa a operação de adição entre os números à
    esquerda e à direita.

    - perform_subtraction(): Executa a operação de subtração entre os números à
    esquerda e à direita.

    - perform_multiplication(): Executa a operação de multiplicação entre os
    números à esquerda e à direita.

    - perform_division(): Executa a operação de divisão entre os números à
    esquerda e à direita.

    - calculate_power(): Calcula a potência do número à esquerda elevado ao
    número à direita.

    - calculate_percentage(): Calcula a porcentagem do número à esquerda em
    relação ao número à direita.

    - root_square(): Calcula a raiz quadrada do número exibido no display.

    - reverse_number(): Inverte o sinal do número exibido no display.

    - calculate_half(): Calcula a metade do número exibido no display.

Observações:
    - Este módulo deve ser importado no módulo principal (main.py)
      para ser utilizado na lógica dos botões da calculadora.

"""
import math
import re
from PySide6.QtWidgets import QGridLayout
from PySide6.QtCore import Slot
from main import Info, Display, Button, MainWindow

NUM_REGEX = re.compile(r'^[0-9]$')


class ButtonsGrid(QGridLayout):
    """
    Classe responsável pela gestão da disposição e funcionalidade dos botões
    em uma calculadora.

    Esta classe herda de QGridLayout e define a organização dos botões em
    linhas e colunas. Ela gerencia as interações do usuário com os botões
    e coordena as operações da calculadora.

    Atributos:
        - _grid_mask (list): Máscara que define a disposição dos botões na
          calculadora.
        - display (Display): Instância da classe Display, responsável por
          exibir os números e resultados.
        - info (Info): Instância da classe Info, usada para exibir a
          equação atual e o resultado.
        - window (MainWindow): Instância da classe MainWindow, que contém
          a janela principal da aplicação.
        - _left (float): Número à esquerda na expressão atual.
        - _right (float): Número à direita na expressão atual.
        - _op (str): Operador atual.
        - _equation (str): String que representa a equação atual.

    Métodos Públicos:
        - __init__: Inicializa a classe ButtonsGrid.
        - create_buttons: Cria os botões para a calculadora e conecta-os
          aos métodos correspondentes.

    Métodos Privados:
        - _connect_button_clicked: Conecta um botão a um slot e define o
          foco no display após a conexão.
        - _make_slot: Cria um slot a partir de uma função com argumentos
          opcionais.

    Métodos de Slots:
        - insert_text_display: Insere texto no display e ajusta o foco.
        - clear_display_and_info: Limpa o display e a informação.
        - is_num: Verifica se uma string é numérica.
        - is_valid_number: Verifica se uma string é um número válido.
        - remove_last_character: Remove o último caractere do display.
        - _get_display_text_stripped: Obtém o texto do display removendo
          espaços em branco à esquerda e à direita.
        - handle_error: Exibe uma caixa de diálogo de erro.
        - _operator_clicked: Lida com o clique em um operador.
        - handle_equal_button_click: Manipula o evento de clique no botão
          de igual (=).
        - perform_operations: Executa as operações com base nos operadores
          e operandos atuais.
        - calculate_percentage: Calcula a porcentagem do número à esquerda
          pelo número à direita.
        - perform_addition: Executa e retorna a adição entre os números à
          esquerda e à direita.
        - perform_subtraction: Executa e retorna a subtração entre os
          números à esquerda e à direita.
        - perform_multiplication: Executa e retorna a multiplicação entre os
          números à esquerda e à direita.
        - perform_division: Executa e retorna a divisão entre os números à
          esquerda e à direita.
        - root_square: Calcula a raiz quadrada do número exibido no display
          e atualiza a equação.
        - reverse_number: Inverte o sinal do número exibido no display.
        - calculate_half: Calcula a metade do número exibido no display.
        - calculate_power: Calcula a potência do número à esquerda elevado ao
          número à direita.
        - handle_large_result: Exibe um erro se o resultado for maior que um
          limite específico.
    """
    def __init__(
            self, _display: Display, _info: Info, window: MainWindow,
            *args, **kwargs) -> None:
        """
        Inicia a classe ButtonsGrid.

        Parâmetros:
            _display (Display): Instância da classe Display, responsável por
                exibir os números e resultados.
            _info (Info): Instância da classe Info, usada para exibir a
                equação atual e o resultado.
            window (MainWindow): Instância da classe MainWindow, que contém
                a janela principal da aplicação.
            *args: Argumentos posicionais adicionais a serem passados para
                a classe pai (QGridLayout).
            **kwargs: Argumentos de palavra-chave adicionais a serem passados
                para a classe pai (QGridLayout).
        """
        super().__init__(*args, **kwargs)

        # Máscara para disposição dos botões na calculadora
        self._grid_mask = [
            ['%', 'CE', 'C', '←'],
            ['½', '^', '√', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['±', '0', '.', '='],
        ]
        # Instâncias dos objetos principais
        self.display = _display
        self.info = _info
        self.window = window

        # Inicialização de variáveis de estado
        self._left = None
        self._right = None
        self._op = None

        self.setSpacing(3)  # Configuração do espaçamento entre os botões
        self._equation = ''  # Inicialização da string de equação
        self.create_buttons()  # Criação dos botões

    @property
    def equation(self):
        """
        Getter para a propriedade 'equation'.

        Retorna:
            str: A equação atual.
        """
        return self._equation

    @equation.setter
    def equation(self, value):
        """
        Setter para a propriedade 'equation'.

        Parâmetros:
            value (str): O novo valor para a equação.
        """
        self._equation = value
        self.info.setText(value)

    def create_buttons(self):
        """
        Cria os botões para a calculadora e conecta-os aos métodos
        correspondentes.

        Este método cria instâncias de botões para cada elemento na máscara
        da grade e os conecta aos métodos apropriados. Também configura a
        aparência dos botões especiais.

        Conexões de Sinal:
            - eq_pressed: Conectado ao método handle_equal_button_click
            - del_pressed: Conectado ao método display.backspace
            - clear_pressed: Conectado ao método clear_display_and_info
            - input_pressed: Conectado ao método insert_text_display
            - operator_pressed: Conectado ao método _operator_clicked
        """
        # Conectar sinais aos métodos correspondentes
        self.display.eq_pressed.connect(self.handle_equal_button_click)
        self.display.del_pressed.connect(self.display.backspace)
        self.display.clear_pressed.connect(self.clear_display_and_info)
        self.display.input_pressed.connect(self.insert_text_display)
        self.display.operator_pressed.connect(self._operator_clicked)

        # Loop para criar e adicionar botões à grade
        for row_number, row in enumerate(self._grid_mask):
            for column, text_grid in enumerate(row):
                _button = Button(text_grid)

                # Configurar botões especiais
                if not self.is_num(text_grid):
                    self._config_special_button(_button)

                    # Configurar a aparência dos botões especiais
                    if _button.text() == '=':
                        _button.setProperty("cssClass", "specialButtonSpace")
                    else:
                        _button.setProperty("cssClass", "specialButton")

                # Adicionar botão à grade
                self.addWidget(_button, row_number, column)

                # Conectar o botão ao método apropriado
                slot = self._make_slot(
                    self.insert_text_display, text_grid)

                self._connect_button_clicked(_button, slot)

    def _connect_button_clicked(self, button, slot):
        """
        Conecta um botão a um slot e define o foco no display após a conexão.

        Este método conecta um botão a um slot específico e, em seguida, define
        o foco no display para garantir uma experiência de usuário contínua.

        Parâmetros:
            - self: Instância da classe ButtonsGrid
            - button: O botão a ser conectado
            - slot: O slot ao qual o botão será conectado

        Returns:
            Nenhum
        """
        button.clicked.connect(slot)
        self.display.setFocus()

    @Slot()
    def _make_slot(self, func, *args, **kwargs):
        """
        Cria um slot a partir de uma função com argumentos opcionais.

        Este método cria um slot que chama a função fornecida com argumentos
        opcionais. Após a execução da função, o foco é definido no display.

        Parâmetros:
            - self: Instância da classe ButtonsGrid
            - func: A função a ser encapsulada no slot
            - *args: Argumentos posicionais a serem passados para a função
            - **kwargs: Argumentos de palavra-chave a serem passados para a
            função

        Returns:
            Nenhum
        """
        @Slot()
        def real_slot():
            func(*args, **kwargs)
            self.display.setFocus()
        return real_slot

    def insert_text_display(self, text):
        """
        Insere texto no display e ajusta o foco.

        Este método insere o texto fornecido no display da calculadora,
        verificando se o resultado seria um número válido. Após a inserção,
        o foco é ajustado para o display.

        Parâmetros:
            - self: Instância da classe ButtonsGrid
            - text: Texto a ser inserido no display

        Returns:
            Nenhum
        """
        new_display_text = self.display.text() + text

        if not self.is_valid_number(new_display_text):
            return

        self.display.insert(text)
        self.display.setFocus()

    def _config_special_button(self, _button):
        """
        Configura ação para botões especiais.

        Este método configura as ações específicas associadas aos botões
        especiais da calculadora, como '=' para realizar a operação,
        '←' para apagar o ultimo valor inserido, 'C' para limpar a calculadora,
        'CE' para limpar o display, '±' para inverter o sinal,
        '½' para calcular a metade e '√' para calcular a raiz quadrada.

        Parâmetros:
            - self: Instância da classe ButtonsGrid
            - _button: Botão a ser configurado

        Returns:
            Nenhum
        """
        text = _button.text()

        # Configurar ação para o botão de igual
        if text == '=':
            self._connect_button_clicked(
                _button, self.handle_equal_button_click)

        # Configurar ação para o botão de retroceder um caracter
        if text == '←':
            self._connect_button_clicked(_button, self.remove_last_character)

        # Configurar ação para o botão de limpar a calculadora
        if text == 'C':
            _button.clicked.connect(self.clear_display_and_info)

        # Configurar ação para o botão de limpar o display
        if text == 'CE':
            _button.clicked.connect(self.display.clear)

        # Configurar ação para o botão de inverter o sinal
        if text == '±':
            _button.clicked.connect(self.reverse_number)

        # Configurar ação para o botão de calcular a metade
        if text == '½':
            _button.clicked.connect(self.calculate_half)

        # Configurar ação para o botão de calcular a raiz quadrada
        if text == '√':
            _button.clicked.connect(self.root_square)

        # Configurar ação para os operadores (+, -, *, /, %, ^)
        if text in '+-*/%^':
            self._connect_button_clicked(
                _button, self._make_slot(
                    self._operator_clicked, _button.text()))

        self.display.setFocus()

    @Slot()
    def clear_display_and_info(self):
        """
        Limpa o display e a informação.

        Este método é chamado quando o botão 'C' é pressionado. Ele limpa o
        conteúdo do display, a informação e redefine as variáveis de operação.

        Parâmetros:
            - self: Instância da classe ButtonsGrid

        Returns:
            Nenhum
        """
        self.display.clear()
        self.info.clear()
        self._op = None
        self._left = None
        self._right = None
        self.display.setFocus()

    @Slot()
    def is_num(self, string: str):
        """
        Verifica se uma string é numérica.

        Este método verifica se a string contém apenas dígitos numéricos.

        Parâmetros:
            - self: Instância da classe ButtonsGrid
            - string: String a ser verificada

        Returns:
            bool: True se a string contiver apenas dígitos numéricos,
            False caso contrário
        """
        return bool(NUM_REGEX.search(string))

    @Slot()
    def is_valid_number(self, string: str):
        """
        Verifica se uma string é um número válido.

        Este método verifica se a string pode ser convertida para um número
        float.

        Parâmetros:
            - self: Instância da classe ButtonsGrid
            - string: String a ser verificada

        Returns:
            bool: True se a string pode ser convertida para float, False caso
            contrário
        """
        valid = False
        try:
            float(string)
            valid = True
        except ValueError:
            valid = False
        return valid

    @Slot()
    def remove_last_character(self):
        """
        Remove o último caractere do display.

        Este método é chamado quando o botão '←' é pressionado. Remove o último
        caractere do display.

        Parâmetros:
            - self: Instância da classe ButtonsGrid

        Returns:
            Nenhum
        """
        if self._get_display_text_stripped():
            new_display = self.display.text()
            self.display.setText(new_display[:-1])
            self.display.setFocus()

    @Slot()
    def _get_display_text_stripped(self):
        """
        Obtém o texto do display removendo espaços em branco à esquerda e à
        direita.

        Este método é usado internamente para obter o texto do display sem
        espaços em branco.

        Parâmetros:
            - self: Instância da classe ButtonsGrid

        Returns:
            str: Texto do display sem espaços em branco à esquerda e à direita
        """
        return self.display.text().strip()

    def handle_error(self, error_message):
        """
        Exibe uma caixa de diálogo de erro.

        Este método é chamado para exibir uma caixa de diálogo com uma mensagem
        de erro.

        Parâmetros:
            - self: Instância da classe ButtonsGrid
            - error_message: Mensagem de erro a ser exibida

        Returns:
            Nenhum
        """
        msg_box = self.window.make_msg_box()
        msg_box.setText(error_message)
        msg_box.setIcon(msg_box.Icon.Critical)
        msg_box.setWindowTitle('ERROR: -> Pablo Alves - Calculator')
        msg_box.exec()
        self.display.setFocus()

    @Slot()
    def _operator_clicked(self, text):
        """
        Lida com o clique em um operador.

        Este método é chamado quando um operador é pressionado. Ele gerencia a
        lógica de cálculo quando os operadores são inseridos.

        Parâmetros:
            - self: Instância da classe ButtonsGrid
            - text: O texto do operador pressionado

        Returns:
            Nenhum
        """
        if self._get_display_text_stripped():

            if self._left is None:

                if self._op is None:
                    # executa se não existir operador e número a esquerda
                    self._left = round(float(self.display.text()), 3)

            else:
                # Se já existe um número à esquerda, executa a operação
                self._right = round(float(self.display.text()), 3)
                self.perform_operations()

        if self._left is not None:
            # Atualiza a equação exibida com o novo operador
            self.equation = f'{self._left} {text} '

        self._op = text
        self.display.clear()
        self.display.setFocus()

    @Slot()
    def handle_equal_button_click(self):
        """
        Manipula o evento de clique no botão de igual (=).

        Este método é chamado quando o botão de igual é pressionado.
        Ele verifica o estado atual da calculadora e executa as operações
        pendentes, se houver, ou atualiza o número à esquerda.

        Se o número à esquerda não estiver definido, o método define o
        número à esquerda como o valor atual no display e limpa o display.
        Caso contrário, define o número à direita como o valor atual no
        display e executa as operações pendentes.

        Conexões de Sinal:
        - eq_pressed: Conectado a este método

        Raises:
            ValueError: Se houver uma entrada inválida, como um texto não
                        numérico no display.

        Parâmetros:
            - self: Instância da classe ButtonsGrid

        Returns:
            Nenhum
        """
        text = self.display.text()

        # Verifica se o texto no display é um número válido
        if self.is_valid_number(text):
            # Manipula resultados grandes
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
        """
        Executa as operações com base nos operadores e operandos atuais.

        Atualiza a equação exibida, chama a função correspondente ao operador
        selecionado e atualiza o número à esquerda com o resultado calculado.

        Conexões de Sinal:
            - Este método é conectado ao clique do botão de igual (=).

        Raises:
            - ZeroDivisionError: Se ocorrer uma divisão por zero durante a
            execução.
            - OverflowError: Se a conta resultar em um valor muito grande para
            ser representado.
            - (TypeError, ValueError): Se ocorrerem erros de tipo ou valor
            durante a execução.

        Returns:
            Nenhum
        """
        # Atualiza a equação exibida
        self.equation = f'{self._left} {self._op} {self._right}'

        # Mapeia operadores para funções correspondentes
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
                # Chama a função correspondente ao operador
                number = round(float(button_functions[self._op]()), 3)
                # Manipula resultados grandes
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
        """
        Calcula e retorna a porcentagem do número à esquerda pelo número
        à direita.
        """
        return round((self._left / 100) * self._right, 3)

    @Slot()
    def perform_addition(self):
        """
        Executa e retorna a adição entre os números à esquerda e à direita.
        """
        return round(self._left + self._right, 3)

    @Slot()
    def perform_subtraction(self):
        """
        Executa e retorna a subtração entre os números à esquerda e à direita.
        """
        return round(self._left - self._right, 3)

    @Slot()
    def perform_multiplication(self):
        """
        Executa e retorna a multiplicação entre os números à esquerda e à
        direita.
        """
        return round(self._left * self._right, 3)

    @Slot()
    def perform_division(self):
        """
        Executa e retorna a divisão entre os números à esquerda e à direita.

        Raises:
            ZeroDivisionError: Se a divisão por zero for detectada.
        """
        return round(self._left / self._right, 3)

    @Slot()
    def root_square(self):
        """
        Calcula a raiz quadrada do número exibido no display e atualiza a
        equação.

        Raises:
            ValueError: Se a entrada não for um número válido.
        """
        try:
            # Obtém o número do display
            number = float(self.display.text())
            #  Verifica se esse número é um número válido
            if self.is_valid_number(number):

                if number < 0:
                    self.handle_error(
                        "A raiz quadrada de número negativo não é definida.")

                # Calcula a raiz quadrada e arredonda para 3 casas decimais
                result = round(math.sqrt(number), 3)
                equation_text = f'√({self.display.text()})'

                # Atualiza a equação com a raiz quadrada
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
        """
        Inverte o sinal do número exibido no display.

        Raises:
            ValueError: Se a entrada não for um número válido.
        """
        try:
            # Obtém o número do display e verifica se é um número válido
            number = float(self.display.text())

            if self.is_valid_number(number):
                # Inverte o sinal do número e atualiza o display
                self.display.setText(str(round(number * -1, 3)))

        except (TypeError, ValueError):
            self.handle_error(
                'Erro de tipo. Verifique os valores inseridos.')

    @Slot()
    def calculate_half(self):
        """
        Calcula a metade do número exibido no display.

        Raises:
            ValueError: Se a entrada não for um número válido.
        """
        try:
            # Obtém o número do display e verifica se é um número válido
            number = float(self.display.text())

            if self.is_valid_number(number):
                # Calcula a metade do número e atualiza o display
                self.display.setText(str(round(0.5 * number, 3)))

        except (TypeError, ValueError):
            self.handle_error(
                'Erro de tipo. Verifique os valores inseridos.')

    @Slot()
    def calculate_power(self):
        """
        Calcula a potência do número à esquerda elevado ao número à direita.

        Raises:
            ValueError: Se a entrada não for um número válido.
        """
        # Calcula a potência e retorna o resultado arredondado
        return round(self._left ** self._right, 3)

    def handle_large_result(self, result):
        """
        Exibe um erro se o resultado for maior que um limite específico.

        Parâmetros:
            result (float): O resultado a ser verificado.

        Returns:
            bool: True se o resultado for maior que o limite, False caso
            contrário.
        """
        limit = 1e15  # Defina o limite conforme necessário

        if float(result) > limit:
            # Exibe uma mensagem de erro se o resultado for muito grande
            error_message = (
                f"O resultado é muito grande para ser exibido.\n"
                f"O resultado é {result:.15f}...")
            self.handle_error(error_message)
            return True

        return False
