from ToSqlConverter.CheckType import CheckType
from ToSqlConverter.TextReader import TextReader
import datetime as dt


class CheckTypeMassive(CheckType, TextReader):
    _type_massive_index = []
    _type_line_list = []
    _data_massive = []

    def __init__(self, path, split_argument) -> None:
        TextReader.__init__(self, path, split_argument)
        self.__create_type_massive()
        self.__create_type_line_list()
        self.__create_data_massive()

    def __create_type_massive(self) -> None:
        massive = self._text_data_massive
        for i in range(len(massive)):
            type_massive_line = []
            for j in range(len(massive[i])):
                type_massive_line.append(self._TYPE_PRIORITY.index(CheckType(massive[i][j]).get_p()))
                if j == range(len(massive[i]))[-1]:
                    self._type_massive_index.append(type_massive_line)
                    # print(type_massive_line)

    def __search_min_index(self) -> []:
        """Search min indexes in massive"""
        index_line = self._type_massive_index[0]
        for i in range(len(self._type_massive_index)):
            for j in range(len(self._type_massive_index[i])):
                if index_line[j] > self._type_massive_index[i][j]:
                    index_line[j] = self._type_massive_index[i][j]
        return index_line

    def __create_type_line_list(self) -> []:
        """Converting an index to a type"""
        self._type_line_list = []
        index_line = self.__search_min_index()
        for i in range(len(index_line)):
            self._type_line_list.append(self._TYPE_PRIORITY[index_line[i]])
        return self._type_line_list

    def get_type_line_list(self) -> [str]:
        return self._type_line_list

    def converting_type(self, argument_type: str, argument: str) -> object:
        if argument_type == self._TYPE_PRIORITY[0]:
            try:
                return argument
            except:
                return None
        elif argument_type == self._TYPE_PRIORITY[1]:
            try:
                return float(argument)
            except:
                return None
        elif argument_type == self._TYPE_PRIORITY[2]:
            try:
                return int(argument)
            except:
                return None
        elif argument_type == self._TYPE_PRIORITY[3]:
            return argument
        else:
            return None

    def __create_data_massive(self):
        massive = self._text_data_massive
        for i in range(len(massive)):
            massive_line = []
            for j in range(len(massive[i])):
                massive_line.append(self.converting_type(self._type_line_list[j], self._text_data_massive[i][j]))
                if j == range(len(massive[i]))[-1]:
                    self._data_massive.append(tuple(massive_line))

    def get_data_massive(self):
        return self._data_massive


