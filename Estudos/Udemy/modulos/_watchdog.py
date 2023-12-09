#  pylint: disable=missing-docstring
# Importa a biblioteca subprocess para executar comandos do sistema
import subprocess

# Importa as classes necessárias da biblioteca watchdog
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path


# Define uma classe personalizada que herda da classe FileSystemEventHandler
class MyHandler(FileSystemEventHandler):
    # Método chamado sempre que ocorre um evento no sistema de arquivos
    def on_any_event(self, event):
        # Verifica se o evento é relacionado a um diretório ou não é um
        # arquivo Python
        if event.is_directory or not event.src_path.endswith('.py'):
            return
        # Imprime uma mensagem indicando a detecção de uma alteração
        print(f'Reloading due to change in {event.src_path}')
        # Executa o script principal (main.py) usando o subprocesso
        subprocess.run(['python', 'main.py'], check=False)


if __name__ == "__main__":
    # Define o caminho do diretório a ser observado (pode ser ajustado conforme
    # necessário)
    PATH_TO_WATCH = Path(__file__)

    # Cria uma instância da classe de manipulador de eventos
    event_handler = MyHandler()

    # Cria uma instância do observador, passando o manipulador de eventos e o
    # caminho do diretório a ser observado
    observer = Observer()
    observer.schedule(event_handler, path=PATH_TO_WATCH, recursive=True)

    # Inicia o observador
    observer.start()

    try:
        # Mantém o programa em execução para continuar observando alterações
        while True:
            pass
    except KeyboardInterrupt:
        # Interrompe o observador se o usuário pressionar Ctrl+C
        observer.stop()

    # Aguarda até que o observador termine
    observer.join()
