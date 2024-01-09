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

# Carrega as variáveis de ambiente a partir do arquivo .env
load_dotenv()

# Define o caminho do arquivo de mensagem HTML
CAMINHO_MSG = Path(__file__).parent / 'msg_confirmacao.html'

# Obtém a data e hora atual no fuso horário 'America/Sao_paulo' e formata
DATA = datetime.now(timezone('America/Sao_paulo')).strftime('%d/%m/%Y\n'
                                                            '%H:%M:%S')
# Configura a localidade para o formato de moeda brasileiro
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Obtém o endereço de e-mail do remetente a partir das variáveis de ambiente
remetente = os.getenv('FROM_EMAIL', '')

# Define o destinatário como o próprio remetente (Apenas para testar)
destinatario = remetente

# Configurações SMTP
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
smtp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('FROM_PASSWORD', '')

# Define os detalhes da compra em um dicionário
compra = {
    'nome': 'Pablo Jr',
    'valor': locale.currency(935.99, grouping=True),
    'data': DATA,
    'servico': 'Automação',
    'numero': '+55 (31) 99423-4449'
}

# Lê o conteúdo do arquivo HTML de mensagem
with open(CAMINHO_MSG, 'r', encoding='utf-8') as email:
    txt = email.read()
    template = Template(txt)
    text_email = template.substitute(compra)

# Tranformar a mensagem em MIMEMultipart
mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Confirmação de compra'

# Adiciona o corpo do e-mail como texto HTML ao objeto MIMEMultipart
corpo_email = MIMEText(text_email, 'html', 'utf-8')
mime_multipart.attach(corpo_email)

# Envia o e-mail usando as configurações SMTP
with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print('Email enviado com sucesso')
