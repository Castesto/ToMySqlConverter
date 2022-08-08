from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode


class ConnectToSql:
    cnx = None
    cursor = None
    DB_NAME = ""

    def __init__(self, user_name, user_password, user_host, user_database):
        self.cnx = mysql.connector.connect(user=user_name,
                                           password=user_password,
                                           host=user_host,
                                           database=user_database)
        self.DB_NAME = user_database
        self.cursor = self.cnx.cursor()
        create_movies_table_query = self.create_table()

        self.cursor.execute(create_movies_table_query)
        self.cnx.commit()


    def create_table(self):
        return f"""
        CREATE TABLE products(
            ID_PRODUCT INT,
            NAME VARCHAR(100),
            CATEGORY VARCHAR(100),
            UNITS VARCHAR(100),
            WEIGHT FLOAT            
        )
        """
p = ConnectToSql('root', 'password', 'localhost', 'product')
