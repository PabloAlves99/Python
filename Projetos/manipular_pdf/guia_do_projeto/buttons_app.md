# Descrição do Código - DefaultButtons

## Introdução

Este arquivo contém a classe `DefaultButtons`, que é responsável por criar e gerenciar os botões da interface gráfica em uma aplicação Python utilizando Tkinter.

## Classe DefaultButtons

### Método `__init__(self, root: Tk, top_frame, bottom_frame, color) -> None`

Construtor da classe `DefaultButtons`.
- Parâmetros:
  - `root`: Objeto Tk da biblioteca Tkinter.
  - `top_frame`: Frame superior da interface gráfica.
  - `bottom_frame`: Frame inferior da interface gráfica.
  - `color`: Objeto contendo informações sobre a paleta de cores da interface.

### Método `create_buttons(self)`

Cria os botões da interface gráfica.

### Método `show_buttons(self)`

Exibe os botões na interface gráfica.

### Método `select_file(self)`

Abre uma janela para selecionar um arquivo PDF.

### Método `update_file_name(self)`

Atualiza o nome do arquivo PDF selecionado na interface gráfica.

### Método `select_folder(self)`

Abre uma janela para selecionar uma pasta de saída.

### Método `update_output_folder_name(self)`

Atualiza o nome da pasta de saída selecionada na interface gráfica.

### Método `extract_text(self)`

Extrai o texto de um arquivo PDF.

### Método `extract_images(self)`

Extrai as imagens de um arquivo PDF.

### Método `save_separate_pdfs(self)`

Salva as páginas de um arquivo PDF individualmente.

### Método `add_pdf_to_pdf_list(self)`

Adiciona arquivos PDF à lista na interface gráfica.

### Método `remove_pdf_to_pdf_list(self, pdf_name)`

Remove um arquivo PDF da lista na interface gráfica.
- Parâmetros:
  - `pdf_name`: Nome do arquivo PDF a ser removido.

### Método `update_listbox(self)`

Atualiza a lista de arquivos PDF na interface gráfica.

### Método `get_selected_pdf(self)`

Obtém o arquivo PDF selecionado na lista da interface gráfica.

### Método `remove_all_list(self)`

Remove todos os arquivos PDF da lista na interface gráfica.

### Método `join_pdf_list(self)`

Une os arquivos PDF da lista na interface gráfica.

## Classes Auxiliares

### Classe `TooltipManager`

Classe para gerenciar tooltips na interface gráfica.
- Métodos:
  - `__init__(self, widget, text)`: Construtor da classe.
  - `bind_events(self)`: Associa eventos de mouse aos widgets.
  - `show_tooltip(self, event)`: Exibe o tooltip quando o mouse passa sobre o widget.
  - `hide_tooltip(self, event)`: Oculta o tooltip quando o mouse sai do widget.

### Classe `HoverEffectManager`

Classe para adicionar efeitos de hover aos botões.
- Métodos:
  - `__init__(self, buttons, hover_color, original_color)`: Construtor da classe.
  - `add_hover_effects(self)`: Adiciona efeitos de hover aos botões.
  - `on_enter(self, button)`: Ativa o efeito de hover quando o mouse passa sobre o botão.
  - `on_leave(self, button)`: Desativa o efeito de hover quando o mouse sai do botão.

