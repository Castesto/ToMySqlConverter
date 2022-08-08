from ToSqlConverter.CheckType import CheckType
from ToSqlConverter.TextReader import TextReader
from ToSqlConverter.CheckTypeMassive import CheckTypeMassive
import os


p = CheckType("2019-06-01 00:00:00")
print(p.get_p())


path = os.path.dirname(__file__) + "/FilesForDB"
print(path)


b = CheckTypeMassive(path + "/transactions", "	")
b.create_type_line_list()
