from ToSqlConverter.CheckType import CheckType
from ToSqlConverter.TextReader import TextReader


class CheckTypeMassive(CheckType, TextReader):

    def __init__(self, argument, path, split_argument):
        CheckType.__init__(self, argument)
        TextReader.__init__(self, path, split_argument)


