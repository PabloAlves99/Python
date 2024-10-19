from datetime import datetime
from tkinter.filedialog import askdirectory
import os


DATA_ATUAL = datetime.now().strftime("%d%m%Y")
SEGUNDO_ATUAL = datetime.now().strftime("%S")
MINUTO_ATUAL = datetime.now().strftime("%M")


caminho = askdirectory(title="Selecione uma pasta")
lista_arquivos = os.listdir(caminho)
extensoes = {
    "imagens": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg", ".ico",
                ".HEIC", '.JPG'],
    "DOCX": [".docx", ".doc"],
    "planilhas": [".xlsx", ".xls", ".csv", ".ods"],
    "pdfs": [".pdf", ".PDF"],
    "texto": [".txt", ".rtf", ".tex",],
    "apresentacoes": [".pptx", ".ppt", ".md"],
    "audio": [".mp3", ".wav", ".ogg", ".flac"],
    "video": [".mp4", ".avi", ".mov", ".wmv", ".m4v", ".REC"],
    "executaveis": [".exe", ".bat", ".sh", ".msi"],
    "compactados": [".zip", ".rar", ".tar.gz"],
    "Python": [".py"],
    "C": [".c", ".h"],
    "C++": [".cpp", ".hpp"],
    "Java": [".java", ".class"],
    "JavaScript": [".js"],
    "HTML": [".html", ".htm"],
    "CSS": [".css"],
    "Ruby": [".rb"],
    "PHP": [".php"],
    "Go": [".go"],
    "TypeScript": [".ts"],
    "SQL": [".sql"],
    "Shell": [".sh"],
    "Perl": [".pl"],
    "R": [".r"],
    "Assembly": [".asm"],
    "JNLP": [".jnlp",],
    "outros": [".bibtex", ".apk", ".xml", ".jar", ".vcf", ".p7s"],
}

arquivos_com_erro_permissao = []

for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")

    for pasta in extensoes:  # pylint: disable=C0206

        if extensao in extensoes[pasta]:
            NOVO_CAMINHO = f'{caminho}/organizador_de_arquivos/'\
                f'{pasta}/{DATA_ATUAL}'
            try:
                if not os.path.exists(NOVO_CAMINHO):
                    os.makedirs(NOVO_CAMINHO)
                os.rename(f"{caminho}/{arquivo}", f"{NOVO_CAMINHO}/{arquivo}")
            except PermissionError:
                arquivos_com_erro_permissao.append(arquivo)
            except FileExistsError:
                if not os.path.exists(NOVO_CAMINHO):
                    os.makedirs(NOVO_CAMINHO)
                os.rename(f"{caminho}/{arquivo}",
                          f"{NOVO_CAMINHO}/{MINUTO_ATUAL}{SEGUNDO_ATUAL}_{arquivo}/")


if arquivos_com_erro_permissao:
    arquivos = '\n'.join(arquivos_com_erro_permissao)
    print(f"Os seguintes arquivos não puderam ser movidos devido a problemas de permissão:\nCaso o arquivo esteja aberto em algum lugar, feche antes de executar o script \n\n{
          arquivos}.")
