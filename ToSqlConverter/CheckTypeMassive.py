from ToSqlConverter.CheckType import CheckType
from ToSqlConverter.TextReader import TextReader


class CheckTypeMassive(CheckType, TextReader):
    _type_massive = []

    def __init__(self, argument, path, split_argument):
        CheckType.__init__(self, argument)
        TextReader.__init__(self, path, split_argument)
        _type_massive = []

    def get_text_line_massive(self) -> str:
        for row in self._text_line_massive:
            for elem in row:
                print(elem, end=' ')

    def create_type_massive(self):
        massive = self._text_line_massive

        for i in range(len(massive)):
            type_massive_line = []
            self._type_massive.append(type_massive_line)
            for j in range(len(massive[i])):
                type_massive_line.append(massive[i][j])
                print(massive[i][j], end=' ')
