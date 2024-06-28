from datetime import datetime
from tkinter.filedialog import askdirectory
import os


CURRENT_DATE = datetime.now().strftime("%d%m%y")
CURRENT_SECOND = datetime.now().strftime("%S")


file_path = askdirectory(title="Selecione uma pasta")
file_list = os.listdir(file_path)
extensions = {
    "imagens": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg", ".ico"],
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
    "outros": [".bibtex", ".apk", ".xml", ".jar"],
}

for _file in file_list:
    name, extension = os.path.splitext(f"{_file}")

    for _folder in extensions:  # pylint: disable=C0206

        if extension.lower() in [ext.lower() for ext in extensions[_folder]]:

            NEW_PATH = os.path.join(
                file_path, 'organizador_de_arquivos', _folder, CURRENT_DATE)

            if not os.path.exists(NEW_PATH):
                os.makedirs(NEW_PATH)

            new_file_path = os.path.join(NEW_PATH, _file)

            try:
                os.rename(os.path.join(file_path, _file), new_file_path)

            except FileExistsError:
                new_file_path = os.path.join(
                    NEW_PATH, f"{CURRENT_SECOND}_{_file}")
                os.rename(os.path.join(file_path, _file), new_file_path)
            break
