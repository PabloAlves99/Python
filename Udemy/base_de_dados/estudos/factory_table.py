# pylint: disable=missing-docstring,empty-docstring
import random
from faker import Faker
import pymysql

fake = Faker('pt_BR')


class FactoryTable():
    table_customers = "CREATE TABLE IF NOT EXISTS Customers( "\
        "ID INT AUTO_INCREMENT PRIMARY KEY, "\
        "FirstName VARCHAR(50)NOT NULL, "\
        "LastName VARCHAR(50) NOT NULL, "\
        "Age INT NOT NULL, "\
        "Email VARCHAR(100) NOT NULL UNIQUE, "\
        "Phone VARCHAR(50) NOT NULL UNIQUE, "\
        "Address_ID INT, "\
        "Job_ID INT, "\
        "FOREIGN KEY(Address_ID) REFERENCES Address(ID_address), "\
        "FOREIGN KEY(Job_ID) REFERENCES Job(ID_job)" \
        ")"

    table_address = "CREATE TABLE IF NOT EXISTS Address("\
        "ID_address INT AUTO_INCREMENT PRIMARY KEY, "\
        "Street VARCHAR(100) NOT NULL, "\
        "Number INT NOT NULL, "\
        "Complement VARCHAR(100), "\
        "Neighbordhood VARCHAR(100), "\
        "City VARCHAR(50) NOT NULL, "\
        "State VARCHAR(50) NOT NULL, "\
        "Country VARCHAR(50) NOT NULL, "\
        "Zipcode VARCHAR(20) NOT NULL"\
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

        self.new_database_connection(
            host_name, user_name, user_password, database_user)

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


class TableJob(FactoryTable):

    _insert_job = "INSERT INTO Job (JobTitle, Salary, "\
        "ExperienceYears, ContractType) "\
        "VALUES (%s, %s, %s, %s)"

    def insert_data_in_job_table(self, data_number: int) -> None:
        cursor = self.connect_to_database()
        try:
            for _ in range(data_number):
                self.__job_method(cursor)
            self._database_connection.commit()
        finally:
            cursor.close()
            self._database_connection.close()

    def _job_method(self, cursor):
        data = self._fake_data_for_job_table()
        cursor.execute(
            self._insert_job,
            (data[0], data[1], data[2], data[3])
        )

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


class TableAddress(FactoryTable):

    _insert_address = "INSERT INTO Address (Street, Number, Complement, "\
        "Neighbordhood, city, state, country, zipcode) "\
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

    def insert_data_in_address_table(self, data_number: int):
        cursor = self.connect_to_database()
        try:
            for _ in range(data_number):
                self.__address_method(cursor)
            self._database_connection.commit()
        finally:
            cursor.close()
            self._database_connection.close()

    def _address_method(self, cursor):
        data = self._fake_data_for_anddress_table()
        cursor.execute(
            f"{self._insert_address}",
            (data[0], data[1], data[2], data[3],
             data[4], data[5], data[6], data[7])
        )

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


class TableCustomers(FactoryTable):

    _insert_customers = "INSERT INTO Customers(FirstName, LastName, Age, "\
        "Email, Phone, Address_ID, Job_ID) "\
        "VALUES ( %s, %s, %s, %s, %s, %s, %s)"

    def insert_data_in_customers_table(self, data_number: int) -> None:
        cursor = self.connect_to_database()
        try:
            for _ in range(data_number):
                self.__customers_method(cursor)
            self._database_connection.commit()
        finally:
            cursor.close()
            self._database_connection.close()

    def _customers_method(self, cursor):
        data = self._fake_data_for_customers_table()
        cursor.execute(
            f"{self._insert_customers}",
            (data[0], data[1], data[2], data[3],
             data[4], data[5], data[6])
        )

    @staticmethod
    def _fake_data_for_customers_table() -> tuple[str, str, int, str,
                                                  str, int, int]:

        first_name = fake.first_name()
        last_name = fake.last_name()
        age = fake.random_int(min=18, max=60)
        email = fake.unique.email()
        phone = fake.unique.phone_number()
        address_id = fake.random_int(min=1, max=30)
        job_id = fake.random_int(min=1, max=30)

        return (first_name, last_name, age, email, phone, address_id, job_id)


class InsertData(TableJob, TableAddress, TableCustomers):

    def __init__(  # pylint: disable=useless-parent-delegation
            self, host_name: str, user_name: str,
            user_password: str, database_user: str) -> None:

        super().__init__(host_name, user_name, user_password, database_user)

    def insert_data_into_all_table(self, data_number: int) -> None:
        cursor = self.connect_to_database()
        try:
            cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
            for _ in range(data_number):
                self._address_method(cursor)
                self._job_method(cursor)
                self._customers_method(cursor)
            cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
            self._database_connection.commit()
        finally:
            cursor.close()
            self._database_connection.close()
