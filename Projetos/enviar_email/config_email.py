"""
Script de envio de e-mail de confirmação de compra.

Este script utiliza a biblioteca smtplib para enviar um e-mail de confirmação
de compra usando um servidor SMTP, e carrega as configurações necessárias a
partir de variáveis de ambiente definidas em um arquivo .env.

Requisitos:
- Bibliotecas: smtplib, email, string, pathlib, datetime, pytz, dotenv

O script realiza as seguintes etapas:
1. Carrega as variáveis de ambiente a partir do arquivo .env.
2. Define o caminho do arquivo de mensagem HTML.
3. Obtém a data e hora atual no fuso horário 'America/Sao_paulo'.
4. Configura a localidade para o formato de moeda brasileiro.
5. Define o remetente e destinatário do e-mail.
6. Configurações SMTP são definidas, incluindo servidor, porta, usuário e senha
7. Cria um dicionário com detalhes da compra.
8. Lê o conteúdo do arquivo HTML de mensagem.
9. Substitui os marcadores no HTML pelos valores da compra.
10. Transforma a mensagem em um objeto MIMEMultipart.
11. Anexa o corpo do e-mail ao objeto MIMEMultipart.
12. Conecta-se ao servidor SMTP, autentica e envia a mensagem.
13. Exibe uma mensagem de sucesso após o envio do e-mail.

Nota: Certifique-se de configurar corretamente as variáveis de ambiente
no arquivo .env.
"""
from ast import main
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


def send_email():

    load_dotenv()
    caminho_msg = Path(__file__).parent / 'msg_confirmacao.html'
    data = datetime.now(timezone('America/Sao_paulo')).strftime('%d/%m/%Y\n'
                                                                '%H:%M:%S')
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    remetente = os.getenv('FROM_EMAIL')
    destinatario = os.getenv('TO_EMAIL')

    # Configurações SMTP
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = remetente
    smtp_password = os.getenv('FROM_PASSWORD')

    # Define os detalhes da compra em um dicionário
    compra = {
        'nome': 'Pablo Jr',
        'valor': locale.currency(935.99, grouping=True),
        'data': data,
        'servico': 'Automação',
        'numero': '+55 (31) 99423-4449'
    }

    # Lê o conteúdo do arquivo HTML de mensagem
    with open(caminho_msg, 'r', encoding='utf-8') as email:
        txt = email.read()
        template = Template(txt)
        text_email = template.substitute(compra)

    # Tranformar a mensagem em MIMEMultipart
    mime_multipart = MIMEMultipart()
    mime_multipart["From"] = remetente
    mime_multipart["To"] = ", ".join(destinatario)
    mime_multipart["Subject"] = 'Confirmação de compra'

    mime_multipart.attach(MIMEText(text_email, 'html', 'utf-8'))

    try:
        # Envia o e-mail usando as configurações SMTP
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.ehlo()
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(remetente, destinatario,
                            mime_multipart.as_string())
            print('Email enviado com sucesso')
    except Exception as e:
        print(f"Erro ao enviar email: {e}")


if __name__ == '__main__':
    send_email()
