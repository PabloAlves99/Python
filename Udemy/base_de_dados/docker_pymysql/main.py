# pylint: disable=all
# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import pymysql
import dotenv
import os
import pymysql.cursors

TABLE_NAME = 'customers'

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'name VARCHAR(50) NOT NULL, '
            'age INT NOT NULL, '
            'PRIMARY KEY (id)'
            ') '
        )
        # Limpa a tabela *** CUIDADO ***
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
    connection.commit()

    # Começa a manipular dados a partir daqui

    # Inserindo um valor usando placeholder
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) '
            'VALUES '
            '(%s, %s)'
        )

        cursor.execute(sql, ("Pablo", 24))
        cursor.execute(sql, ("Henrique", 23))
        cursor.execute(sql, ("Jr", 22))
    connection.commit()

    # Inserindo um valor usando placeholder e um dicionário
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) '
            'VALUES '
            '(%(name)s, %(age)s)'
        )

        data = {
            "name": "Alves",
            "age": 20
        }
        cursor.execute(sql, data)
    connection.commit()

    # Inserindo vários valores usando placeholder e um tupla de dicionários
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) '
            'VALUES '
            '(%(name)s, %(age)s)'
        )

        data2 = (
            {"name": "Julia", "age": 27},
            {"name": "Lucas", "age": 24},
            {"name": "Beatriz", "age": 29},
            {"name": "Gustavo", "age": 26},
            {"name": "Camila", "age": 31},
            {"name": "Miguel", "age": 23},
            {"name": "Isabel", "age": 33},
            {"name": "Rafael", "age": 21},
            {"name": "Larissa", "age": 35},
            {"name": "Anderson", "age": 34},
        )
        cursor.executemany(sql, data2)
    connection.commit()

    # Inserindo vários valores usando placeholder e um tupla de tuplas
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) '
            'VALUES '
            '(%s, %s)'
        )

        data4 = (
            ("João", 25),
            ("Maria", 30),
            ("Carlos", 22),
            ("Ana", 28),
            ("Pedro", 32),
        )
        cursor.executemany(sql, data4)
    connection.commit()

    # Lendo os valores com SELECT
    with connection.cursor() as cursor:
        # SMALLER = int(input('Digite o menor id: '))
        # BIGGER = int(input('Digite o maior id: '))
        SMALLER = 5
        BIGGER = 10

        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE id BETWEEN %s AND %s '
        )

        cursor.execute(sql, (SMALLER, BIGGER))
        # print(cursor.mogrify(sql, (SMALLER, BIGGER)))

        data5 = cursor.fetchall()
        # print(*data5, sep='\n')

    # Apagando com DELETE e WHERE no PyMySQL
    with connection.cursor() as cursor:

        sql = (
            f'DELETE FROM {TABLE_NAME} '
            'WHERE id = 5'
        )
        cursor.execute(sql)
        connection.commit()

        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')
        # print(*cursor.fetchall(), sep='\n')

    # Editando com UPDATE, WHERE e placeholders no PyMySQL
    with connection.cursor() as cursor:

        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET name = %s, age = %s '
            'WHERE id = %s'
        )
        cursor.execute(sql, ('UPDATE', 99, 3))

        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        print(*cursor.fetchall(), sep='\n')

    connection.commit()
