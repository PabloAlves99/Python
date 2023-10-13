import pyaudio
import wave

audio = pyaudio.PyAudio()

stream = audio.open(
    input=True,
    format=pyaudio.paInt16, # Formato de amplitude de 16 bits
    channels=1, # Define quantos canal de audio 
    rate=44000, # Basicamente é a taxa do audio
    frames_per_buffer=1024, # tamanho dos "bloquinhos" de audio
)

frames = []

try:
    while True:
        bloco = stream.read(1024)
        frames.append(bloco)
except KeyboardInterrupt:
    pass

stream.start_stream() 
stream.close()
audio.terminate() 
arquivo_final = wave.open("gravacao.wav", "wb") #  wb = para escrever em formato de bits

# configurando com as mesmas configurações passadas
arquivo_final.setnchannels(1) 
arquivo_final.setframerate(44000) 
arquivo_final.setsampwidth(audio.get_sample_size(pyaudio.paInt16)) 

arquivo_final.writeframes(b"".join(frames)) 
arquivo_final.close()