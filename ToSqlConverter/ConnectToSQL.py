from __future__ import print_function
from ToSqlConverter.ColumnTables import get_columns
import mysql.connector
from mysql.connector.connection_cext import CMySQLConnection
from mysql.connector.cursor_cext import CMySQLCursor


class ConnectToSql:
    __cnx: CMySQLConnection
    __cursor: CMySQLCursor

    def __init__(self, user_name: str, user_password: str, user_host: str, user_database: str) -> None:
        self.__cnx = mysql.connector.connect(user=user_name,
                                             password=user_password,
                                             host=user_host,
                                             database=user_database)
        self.DB_NAME = user_database
        self.__cursor = self.__cnx.cursor()
        create_movies_table_query = None

        self.__cursor.execute(create_movies_table_query)
        self.__cnx.commit()


    def create_table(self) -> None:
        return """
        CREATE TABLE products_data_all(
            ID_PRODUCT INT,
            NAME VARCHAR(100),
            CATEGORY VARCHAR(100),
            UNITS VARCHAR(10),
            WEIGHT FLOAT,
            PRICE int,
            DATE_UPD DATETIME,
            ID_STORE INT,
            NAME_STORE VARCHAR(100)                        
        )
        """

    def insert_into_table(self, table_name: str, data_massive: []) -> None:
        columns = getattr(get_columns(), table_name)
        count_column = ", ".join(["%s"] * len(columns))
        names_column = ", ".join(columns)
        sql = f"INSERT INTO {table_name} ({names_column}) VALUES ({count_column})"
        for i in range(len(data_massive)-1):
            val = data_massive[i]
            self.__cursor.execute(sql, val)
            self.__cnx.commit()






