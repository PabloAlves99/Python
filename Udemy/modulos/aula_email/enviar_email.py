import os
import locale
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
from pathlib import Path
from datetime import datetime
from pytz import timezone
from dotenv import load_dotenv

load_dotenv()

CAMINHO_MSG = Path(__file__).parent / 'msg_confirmacao.html'
DATA = datetime.now(timezone('America/Sao_paulo')).strftime('%d/%m/%Y\n'
                                                            '%H:%M:%S')
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

remetente = os.getenv('FROM_EMAIL', '')
destinatario = remetente

# Configurações SMTP
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
smtp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('FROM_PASSWORD', '')

compra = {
    'nome': 'Pablo Jr',
    'valor': locale.currency(935.99, grouping=True),
    'data': DATA,
    'servico': 'Automação',
    'numero': '+55 (31) 99423-4449'
}

# Mensagem de texto
with open(CAMINHO_MSG, 'r', encoding='utf-8') as email:
    txt = email.read()
    template = Template(txt)
    text_email = template.substitute(compra)

# Tranformar a mensagem em MIMEMultipart
mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Confirmação de compra'

corpo_email = MIMEText(text_email, 'html', 'utf-8')
mime_multipart.attach(corpo_email)

# Enviar email
with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print('Email enviado com sucesso')
