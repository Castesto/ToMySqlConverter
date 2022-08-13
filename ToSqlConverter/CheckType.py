import datetime as dt


class CheckType:

    _TYPE_PRIORITY = ["datetime", "float", "int", "string", "Null"]
    _p: str
    _date_formatter = "%Y-%m-%d %H:%M:%S"

    def __init__(self, argument: str):
        self._p: str = self.__check_type(argument)

    def __is_int(self, argument) -> bool:
        try:
            return isinstance(int(argument), int)
        except ValueError:
            return False

    def __is_float(self, argument: str) -> bool:
        try:
            return isinstance(float(argument), float)
        except ValueError:
            return False

    def __is_date(self, argument: str) -> bool:
        try:
            date_formatter = "%Y-%m-%d %H:%M:%S"
            dt.datetime.strptime(argument, date_formatter)
            return True
        except TypeError:
            return False
        except ValueError:
            return False

    def __is_string(self, argument: str) -> bool:
        try:
            return isinstance(str(argument), str)
        except ValueError:
            return False

    def get_p(self) -> str:
        return self._p

    def __check_type(self, argument: str):
        if argument == self._TYPE_PRIORITY[4]:
            return self._TYPE_PRIORITY[4]
        elif self.__is_date(argument):
            return self._TYPE_PRIORITY[0]
        elif self.__is_int(argument):
            return self._TYPE_PRIORITY[2]
        elif self.__is_float(argument):
            return self._TYPE_PRIORITY[1]
        elif self.__is_string(argument):
            return self._TYPE_PRIORITY[3]
        else:
            return "No matches"

