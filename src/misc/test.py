import os
from dotenv import load_dotenv
from mysql.connector import connect, Error

#Secrets
load_dotenv()

PREFIX = os.getenv("PREFIX")
TOKEN = os.getenv("TOKEN")
MAX_QUOTE_LENGTH = int(os.getenv("MAX_QUOTE_LENGTH"))
SQL_USERNAME = os.getenv("SQL_USERNAME")
SQL_PASSWORD = os.getenv("SQL_PASSWORD")
DATABASE = os.getenv("DATABASE")

#Connecting to database
try:
    with connect(
        host="localhost",
        user=SQL_USERNAME,
        password=SQL_PASSWORD,
        database=DATABASE,
    ) as connection:
        print(connection)
        msg = "asdsadadasdad  asdad as"
        insert_query = f"INSERT INTO quotes (quote) VALUES ('{msg}')"
        print(insert_query)
        with connection.cursor() as cursor:
            cursor.execute(insert_query)
            connection.commit()
            cursor.execute("SELECT * FROM quotes")
            result = cursor.fetchall()
            for row in result:
                print(row)

#         create_movies_table_query = """
#         CREATE TABLE quotes(
#             id INT AUTO_INCREMENT PRIMARY KEY,
#             quote VARCHAR(600),
#             author VARCHAR(32)
#         )
#         """
#         with connection.cursor() as cursor:
#             cursor.execute("USE quotes_db")
#             cursor.execute(create_movies_table_query)
#             connection.commit()

except Error as e:
    print(e)