# pylint: disable=all
import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)

cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

connection.commit()

# Registra valores nas colunas da tabela
cursor.execute(
    f'INSERT INTO {TABLE_NAME} (id, name, weight)'
    'VALUES '
    '(NULL, "Pablo Alves","10"), (NULL, "Pablo Junior","7")'
)

connection.commit()

cursor.close()
connection.close()
