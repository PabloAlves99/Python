import os

from dotenv import load_dotenv

load_dotenv()

remetente = os.getenv('FROM_EMAIL', '')
destinatario = remetente
