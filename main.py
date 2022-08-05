from ToSqlConverter.CheckType import CheckType
from ToSqlConverter.TextReader import TextReader
from ToSqlConverter.CheckTypeMassive import CheckTypeMassive
import os


p = CheckType("22-11-2000 0:00:00")
print(p.get_p())


path = os.path.dirname(__file__) + "/FilesForDB"
print(path)


b = CheckTypeMassive("22-11-2000 0:00:00", path + "/transactions", "	")
b.create_type_massive()

