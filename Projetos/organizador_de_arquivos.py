import os
from tkinter.filedialog import askdirectory
from datetime import datetime
from pytz import timezone


caminho = askdirectory(title="Selecione uma pasta")
DATA = datetime.now(timezone('America/Sao_paulo')).strftime('%d%m%Y')

lista_arquivos = os.listdir(caminho)

extensoes = {
    "oa_imagens": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg", ".ico"],
    "oa_DOCX": [".docx", ".doc"],
    "oa_planilhas": [".xlsx", ".xls", ".csv", ".ods"],
    "oa_pdfs": [".pdf", ".PDF"],
    "oa_texto": [".txt", ".rtf", ".tex",],
    "oa_apresentacoes": [".pptx", ".ppt", ".md"],
    "oa_audio": [".mp3", ".wav", ".ogg", ".flac"],
    "oa_video": [".mp4", ".avi", ".mov", ".wmv"],
    "oa_executaveis": [".exe", ".bat", ".sh", ".msi", ".jar"],
    "oa_compactados": [".zip", ".rar", ".tar.gz"],
    "oa_Python": [".py"],
    "oa_C": [".c", ".h"],
    "oa_C++": [".cpp", ".hpp"],
    "oa_Java": [".java", ".class"],
    "oa_JavaScript": [".js"],
    "oa_HTML": [".html", ".htm"],
    "oa_CSS": [".css"],
    "oa_Ruby": [".rb"],
    "oa_PHP": [".php"],
    "oa_Go": [".go"],
    "oa_TypeScript": [".ts"],
    "oa_SQL": [".sql"],
    "oa_Shell": [".sh"],
    "oa_Perl": [".pl"],
    "oa_R": [".r"],
    "oa_Assembly": [".asm"],
    "oa_outros": [".bibtex"],
}

for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")

    for pasta in extensoes:  # pylint: disable=C0206

        if extensao in extensoes[pasta]:

            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")

            os.rename(f"{caminho}/{arquivo}",
                      f"{caminho}/{pasta}/{DATA},{arquivo}")
