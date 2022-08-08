from ToSqlConverter.CheckType import CheckType
from ToSqlConverter.TextReader import TextReader
from ToSqlConverter.CheckTypeMassive import CheckTypeMassive
import os


path = os.path.dirname(__file__) + "/FilesForDB"

b = CheckTypeMassive(path + "/transactions", "	")
print(b.create_type_line_list())
