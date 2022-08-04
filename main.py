from ToSqlConverter.CheckType import CheckType
from ToSqlConverter.TextReader import TextReader
from ToSqlConverter.CheckTypeLine import CheckTypeMassive
import os


p = CheckType("22-11-2000 0:00:00")
print(p.get_p())

path = os.path.dirname(__file__) + "/FilesForDB"
print(path)

a = TextReader(path + "/products", "	")
print(a.get_text_line_massive())
b = CheckTypeMassive("22-11-2000 0:00:00", path + "/transactions", "	")
print(b.get_text_line_massive())
