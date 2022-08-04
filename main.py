from ToSqlConverter.CheckType import CheckType
from ToSqlConverter.TextReader import TextReader

p = CheckType("22-11-2000 0:00:00")
print(p.get_p())
a = TextReader("C:/Users/User/PycharmProjects/pythonProject/FilesForDB/transactions", "	")
print(a.get_text_line_massive())
b = TextReader("C:/Users/User/PycharmProjects/pythonProject/FilesForDB/products", "	")
print(b.get_text_line_massive())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
