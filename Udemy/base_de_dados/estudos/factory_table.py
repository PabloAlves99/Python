# pylint: disable=missing-docstring,empty-docstring
import random
from faker import Faker
import pymysql

fake = Faker('pt_BR')


class FactoryTable():
    table_customers = "CREATE TABLE IF NOT EXISTS customers( "\
        "ID INT AUTO_INCREMENT PRIMARY KEY, "\
        "FirstName VARCHAR(50)NOT NULL, "\
        "LastName VARCHAR(50) NOT NULL, "\
        "Age INT NOT NULL, "\
        "Email VARCHAR(100) NOT NULL UNIQUE, "\
        "Phone VARCHAR(50) NOT NULL UNIQUE, "\
        "Address_ID INT, "\
        "Job_ID INT, "\
        "FOREIGN KEY(Address_ID) REFERENCES Address(ID_address), "\
        "FOREIGN KEY(job_ID) REFERENCES Job(ID_job)" \
        ")"

    table_address = "CREATE TABLE IF NOT EXISTS Address("\
        "ID_address INT AUTO_INCREMENT PRIMARY KEY, "\
        "Street VARCHAR(100) NOT NULL, "\
        "Number INT NOT NULL, "\
        "Complement VARCHAR(100), "\
        "Neighbordhood VARCHAR(100), "\
        "city VARCHAR(50) NOT NULL, "\
        "state VARCHAR(50) NOT NULL, "\
        "country VARCHAR(50) NOT NULL, "\
        "zipcode VARCHAR(20) NOT NULL"\
        ")"

    table_job = "CREATE TABLE IF NOT EXISTS Job ("\
        "ID_job INT AUTO_INCREMENT PRIMARY KEY, "\
        "JobTitle VARCHAR(100) NOT NULL, "\
        "Salary DECIMAL(10, 2) NOT NULL, "\
        "ExperienceYears INT, "\
        "ContractType VARCHAR(50) NOT NULL"\
        ")"

    def __init__(
            self, host_name: str, user_name: str,
            user_password: str, database_user: str
    ):

        self._database_connection = pymysql.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=database_user
        )

    def new_database_connection(
            self, host_name: str, user_name: str,
            user_password: str, database_user: str) -> None:

        self._database_connection = pymysql.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=database_user,
        )

    def connect_to_database(self):
        return self._database_connection.cursor()

    def create_all_tables(self):
        cursor = self.connect_to_database()
        try:
            cursor.execute(self.table_address)
            cursor.execute(self.table_job)
            cursor.execute(self.table_customers)

            self._database_connection.commit()
        finally:
            cursor.close()
            self._database_connection.close()


class InsertData(FactoryTable):

    def __init__(  # pylint: disable=useless-parent-delegation
            self, host_name: str, user_name: str,
            user_password: str, database_user: str) -> None:

        super().__init__(host_name, user_name, user_password, database_user)

    def insert_data_in_job_table(self, data_number: int) -> None:
        cursor = self.connect_to_database()
        try:
            for _ in range(data_number):
                data = self._fake_data_for_job_table()
                cursor.execute(
                    "INSERT INTO Job (JobTitle, Salary, "
                    "ExperienceYears, ContractType) "
                    f"VALUES ('{data[0]}', '{data[1]}', "
                    f"{data[2]}, '{data[3]}')"
                )
            self._database_connection.commit()
        finally:
            cursor.close()
            self._database_connection.close()

    @staticmethod
    def _fake_data_for_job_table() -> tuple[str, int, int, str]:

        title_job = fake.job()

        salary = random.randint(1000, 20000)

        regimes_contrato_trabalho = [
            "Tempo Integral",
            "Meio Período",
            "Contrato por Hora",
            "Contrato por Projeto",
            "Trabalho Remoto",
            "Trabalho Temporário",
            "Estágio",
            "Freelance",
            "Trabalho Autônomo",
        ]

        return (
            title_job, salary, random.randint(1, 35),
            random.choice(regimes_contrato_trabalho)
        )

    def insert_data_in_address_table(self, data_number):
        cursor = self.connect_to_database()
        try:
            for _ in range(data_number):
                data = self._fake_data_for_anddress_table()
                cursor.execute(
                    "INSERT INTO Address (Street, Number, Complement, "
                    "Neighbordhood, city, state, country, zipcode) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                    (data[0], data[1], data[2], data[3],
                     data[4], data[5], data[6], data[7])
                )
            self._database_connection.commit()
        finally:
            cursor.close()
            self._database_connection.close()

    @staticmethod
    def _fake_data_for_anddress_table() -> tuple[str, int, str,
                                                 str, str, str, str, str]:
        street = fake.street_name()
        number = fake.building_number()
        complement = ('Casa', 'Apartamento', 'Condominio', 'Hotel')
        neighbordhood = fake.city_suffix()
        city = fake.city()
        state = fake.state()
        country = fake.country()
        zipcode = random.randint(1234567, 9999999)

        return (street, int(number), random.choice(complement), neighbordhood,
                city, state, country, str(zipcode))
