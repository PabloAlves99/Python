# pylint: disable=missing-docstring,empty-docstring
import os
import smtplib

from typing import List, Union
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
from mensagem_email import EmailBody


class SendEmail:

    def __init__(
            self, _remetente: Union[str, None] = None,
            _password: Union[str, None] = None,
            _destinatarios: Union[str, None] = None, *args: List[str]) -> None:

        self.contador_emails: int = 0
        self.emails_enviados: List[str] = []
        self.fill_email_data(_remetente, _password, _destinatarios, *args)
        self.initialize_smtp_config()
        self.get_text_email()
        self.send_emails()
        self.display_email_result()

    def fill_email_data(
            self, _remetente, _password, _destinatarios, *args) -> None:

        load_dotenv()
        if args:
            if len(args) == 3:
                _remetente, _password, _destinatarios = args
            else:
                raise ValueError(
                    "Número incorreto de argumentos não nomeados."
                    "Esperava-se 3.")

        self.remetente = _remetente if _remetente is not None else os.getenv(
            'FROM_EMAIL')
        self.password = _password if _password is not None else os.getenv(
            'FROM_PASSWORD')
        self.destinatarios = _destinatarios if _destinatarios is not None else os.getenv(
            'TO_EMAIL').split(',')

    def initialize_smtp_config(self) -> None:
        self.smtp_server = 'smtp.gmail.com'
        self.smtp_port = 587
        self.smtp_username = self.remetente
        self.smtp_password = self.password

    def get_text_email(self) -> None:
        email_body = EmailBody()
        self.text_email = email_body.text_email

    def send_emails(self) -> None:
        for destinatario in self.destinatarios:
            destinatario = destinatario.strip()  # Remover espaços em branco
            # Transformar a mensagem em MIMEMultipart
            mime_multipart = MIMEMultipart()
            mime_multipart["From"] = self.remetente
            mime_multipart["To"] = destinatario
            mime_multipart["Subject"] = 'Confirmação de compra'

            mime_multipart.attach(MIMEText(self.text_email, 'html', 'utf-8'))

            try:
                # Envia o e-mail usando as configurações SMTP
                with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                    self.contador_emails += 1
                    print(f'\nDestinatário {
                        self.contador_emails}: {destinatario}')
                    server.ehlo()
                    server.starttls()
                    server.login(self.smtp_username, self.smtp_password)
                    server.sendmail(self.remetente, destinatario,
                                    mime_multipart.as_string())
                    print("Verificações concluídas")
                self.emails_enviados.append(destinatario)
            except smtplib.SMTPAuthenticationError:
                print(
                    "Erro de autenticação: verifique o email e a senha do "
                    "remetente."
                )
            except smtplib.SMTPConnectError:
                print(
                    "Erro de conexão: não foi possível conectar ao servidor "
                    "SMTP."
                )
            except smtplib.SMTPRecipientsRefused:
                print(
                    f"Erro: {destinatario} foi recusado pelo servidor SMTP."
                )
            except smtplib.SMTPSenderRefused:
                print("Erro: O remetente foi recusado pelo servidor SMTP.")
            except smtplib.SMTPDataError:
                print("Erro: O servidor SMTP retornou um erro ao enviar os "
                      "dados.")
            except smtplib.SMTPException as e:
                print(f"Erro SMTP: {e}")
            except Exception as e:
                print(f"Erro não identificado ao enviar email: {e}")

    def display_email_result(self) -> None:
        if self.emails_enviados:
            print(f'\nEmail enviado com sucesso para:\n\n'
                  f'{"\n".join(
                      [email.strip() for email in self.emails_enviados])}')
        else:
            print('\nNenhum email enviado')


if __name__ == '__main__':
    SendEmail()
