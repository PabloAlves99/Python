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

cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)

connection.commit()

# Registra valores nas colunas da tabela
# CUIDADO: sql injection
sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES '
    # '(?, ?)'
    '(:name, :weight)'
)
# cursor.execute(sql, ['Pablo', 8])
# cursor.executemany(sql, [['Pablo', 8], ['Henrique', 7], ['Junior', 10]])
cursor.executemany(sql, (
    {'name': 'Pablo', 'weight': 7},
    {'name': 'Pablo Silva', 'weight': 8},
    {'name': 'Pablo Alves', 'weight': 9},
    {'name': 'Pablo Henrique', 'weight': 10},
    {'name': 'Pablo Junior', 'weight': 11},
))
connection.commit()

print(sql)

cursor.close()
connection.close()
