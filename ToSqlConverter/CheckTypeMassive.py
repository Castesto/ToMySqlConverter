from ToSqlConverter.CheckType import CheckType
from ToSqlConverter.TextReader import TextReader


class CheckTypeMassive(CheckType, TextReader):
    _type_massive_index = []
    _type_massive = []
    _type_line_list = []

    def __init__(self, path, split_argument):
        TextReader.__init__(self, path, split_argument)
        self.create_type_massive()

    def create_type_massive(self) -> None:
        massive = self._text_line_massive
        for i in range(len(massive)):
            type_massive_line = []
            for j in range(len(massive[i])):
                type_massive_line.append(self._TYPE_PRIORITY.index(CheckType(massive[i][j]).get_p()))
                if j == range(len(massive[i]))[-1]:
                    self._type_massive_index.append(type_massive_line)
                    # print(type_massive_line)

    def search_min_index(self):
        index_line = self._type_massive_index[0]
        for i in range(len(self._type_massive_index)):
            for j in range(len(self._type_massive_index[i])):
                if index_line[j] > self._type_massive_index[i][j]:
                    index_line[j] = self._type_massive_index[i][j]
        return index_line

    def create_type_line_list(self):
        self._type_line_list = []
        index_line = self.search_min_index()
        for i in range(len(index_line)):
            self._type_line_list.append(self._TYPE_PRIORITY[index_line[i]])
        print(self._type_line_list)


