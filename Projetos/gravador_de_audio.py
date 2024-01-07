"""
Script de Gravação de Áudio

Este script utiliza a biblioteca PyAudio para gravar áudio de entrada contínua
e salvar a gravação em um arquivo WAV chamado 'gravacao.wav' na mesma pasta do
script.

Dependências:
    - PyAudio (instalável com 'pip install pyaudio')

Instruções de Uso:
    1. Execute este script para iniciar a gravação.
    2. Pressione Ctrl+C para interromper a gravação.
    3. O arquivo 'gravacao.wav' será salvo na mesma pasta do script.

Notas:
    - Certifique-se de ter as dependências instaladas antes de executar o
    script.
    - Este script é uma demonstração básica e pode ser expandido conforme
    necessário.

Autor: Pablo Alves
Data: 07/01

Exemplo de Uso:
    ```bash
    python gravador_de_audio.py
    ```
"""
#  pylint: disable= all
import pyaudio
import wave
import os

audio = pyaudio.PyAudio()

# Configuração do stream de áudio
stream = audio.open(
    input=True,
    format=pyaudio.paInt16,  # Formato de amplitude de 16 bits
    channels=1,  # Define quantos canal de audio
    rate=44000,  # Basicamente é a taxa do audio
    frames_per_buffer=1024,  # tamanho dos "bloquinhos" de audio
)

# Lista para armazenar os blocos de áudio
frames = []

try:
    # Loop infinito para capturar os blocos de áudio até uma interrupção do
    # teclado
    while True:
        block = stream.read(1024)
        frames.append(block)
except KeyboardInterrupt:
    pass

# Encerra o stream e o PyAudio
stream.start_stream()
stream.close()
audio.terminate()

# Obtém o diretório do script
script_folder = os.path.dirname(os.path.abspath(__file__))

# Criação do caminho completo para o arquivo WAV na mesma pasta do script
wave_path = os.path.join(script_folder, "gravacao.wav")

# Criação do arquivo WAVE para armazenar a gravação
# 'wb' para escrever em formato binário
final_file = wave.open(wave_path, "wb")

# Configuração do arquivo WAVE com as mesmas configurações do stream
final_file.setnchannels(1)
final_file.setframerate(44000)
final_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))

# Escreve os blocos de áudio no arquivo WAVE
final_file.writeframes(b"".join(frames))

final_file.close()
