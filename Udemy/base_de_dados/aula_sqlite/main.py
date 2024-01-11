# pylint: disable=all
import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CRUD - Creat   Read    Update  Delete
# SQL  - INSERT  SELECT  UPDATE  DELETE

# CUIDADO: Fazendo delete sem where
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

# Delete mais cuidadoso
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)

# Criar a tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)

connection.commit()

# Registra valores nas colunas da tabela
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


if __name__ == '__main__':
    print(sql)

    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id = "3"'
    )
    connection.commit()

    cursor.execute(
        f'UPDATE {TABLE_NAME} '
        'SET name="QUALQUER" '
        'WHERE id = "2"'
    )
    connection.commit()

    cursor.execute(
        f'SELECT * FROM {TABLE_NAME}'
    )

    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight)

    cursor.close()
    connection.close()
