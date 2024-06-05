import os
from pprint import pprint
from factory_table import InsertData
import dotenv


if __name__ == "__main__":

    dotenv.load_dotenv()

    estudos = InsertData(host_name=os.environ['bd_host_name'],
                         user_name=os.environ['bd_user_name'],
                         user_password=os.environ['bd_user_password'],
                         database_user=os.environ['bd_database_user'])
    # estudos.create_all_tables()
    # estudos.insert_data_in_job_table(10)
    # estudos.insert_data_in_customers_table(40)
    # estudos.insert_data_in_address_table(10)
    # estudos.insert_data_into_all_table(5)

    cursor = estudos.connect_to_database()
    try:
        cursor.execute(
            "SELECT * FROM Job"
        )
        rows = cursor.fetchall()
    finally:
        cursor.close()
    pprint(rows)
