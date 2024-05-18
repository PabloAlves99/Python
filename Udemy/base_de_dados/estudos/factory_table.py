# pylint: disable=missing-docstring,empty-docstring

import pymysql


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

    # def create_customers(self):
    #     cursor = self.connect_to_database()

    #     cursor.execute(self.table_customers)
    #     self._database_connection.commit()

    # def create_address(self):
    #     cursor = self.connect_to_database()

    #     cursor.execute(self.table_address)
    #     self._database_connection.commit()

    # def create_job(self):
    #     cursor = self.connect_to_database()

    #     cursor.execute(self.table_job)
    #     self._database_connection.commit()
