from ToSqlConverter.CheckType import CheckType
from ToSqlConverter.TextReader import TextReader
from ToSqlConverter.ConnectToSQL import ConnectToSql
from ToSqlConverter.CheckTypeMassive import CheckTypeMassive
import os
import datetime as dt


path = os.path.dirname(__file__) + "/FilesForDB"

b = CheckTypeMassive(path + "/products_stores", "	")

connect_to_sql = ConnectToSql('root', 'password', 'localhost', 'product')
# connect_to_sql.insert_into_table("products_stores", b.get_data_massive())
# print(tuple(b.get_data_massive()))