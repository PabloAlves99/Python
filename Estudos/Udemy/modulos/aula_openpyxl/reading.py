from pathlib import Path

from openpyxl import load_workbook

ROOT_FOLDER = Path(__file__).parent
WORKBOOK_PATH = ROOT_FOLDER / 'workbook.xlsx'

workbook = load_workbook(WORKBOOK_PATH)
# worksheet: Worksheet = workbook.active

# Nome para a planilha
SHEET_NAME = 'Minha planilha'

# Selecionou a planilha
worksheet = workbook[SHEET_NAME]


# workbook.save(WORKBOOK_PATH)
