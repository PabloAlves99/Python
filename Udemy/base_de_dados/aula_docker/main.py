# pylint: disable=all
# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import pymysql
import dotenv
import os

TABLE_NAME = 'customers'

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4'
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
    with connection.cursor() as cursor:
        sql = (f'INSERT INTO {TABLE_NAME} '
               '(name, age) '
               'VALUES '
               '(%s, %s)')

        cursor.execute(sql, ("Pablo", 24))
        cursor.execute(sql, ("Henrique", 23))
        cursor.execute(sql, ("Jr", 22))
    connection.commit()

    with connection.cursor() as cursor:
        sql = (f'INSERT INTO {TABLE_NAME} '
               '(name, age) '
               'VALUES '
               '(%(name)s, %(age)s)')

        data = {
            "name": "Alves",
            "age": 20
        }
        result = cursor.execute(sql, data)
    connection.commit()

    with connection.cursor() as cursor:
        sql = (f'INSERT INTO {TABLE_NAME} '
               '(name, age) '
               'VALUES '
               '(%(name)s, %(age)s)')

        data2 = [
            {"name": "João", "age": 25},
            {"name": "Maria", "age": 30},
            {"name": "Carlos", "age": 22},
            {"name": "Ana", "age": 28},
            {"name": "Pedro", "age": 32},
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
        ]
        result2: int | None = cursor.executemany(sql, data2)
        print(sql)
        print(*data2, sep='\n')
        print(result2)
    connection.commit()
