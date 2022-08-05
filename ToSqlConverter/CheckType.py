import datetime as dt


class CheckType:

    _TYPE = ["string", "float", "int", "datetime", "nan"]
    _p: str = "none"

    def __init__(self, argument):
        if argument == self._TYPE[4]:
            self._p = self._TYPE[4]
        elif self.__is_date(argument):
            self._p = self._TYPE[3]
        elif self.__is_int(argument):
            self._p = self._TYPE[2]
        elif self.__is_float(argument):
            self._p = self._TYPE[1]
        elif self.__is_string(argument):
            self._p = self._TYPE[0]
        else:
            self._p = "No matches"

    def __is_int(self, argument) -> bool:
        try:
            return isinstance(int(argument), int)
        except ValueError:
            return False

    def __is_float(self, argument) -> bool:
        try:
            return isinstance(float(argument), float)
        except ValueError:
            return False

    def __is_date(self, argument) -> bool:
        try:
            date_formatter = "%Y-%m-%d %H:%M:%S"
            dt.datetime.strptime(argument, date_formatter)
            return True
        except ValueError:
            return False

    def __is_string(self, argument) -> bool:
        try:
            return isinstance(str(argument), str)
        except ValueError:
            return False

    def get_p(self) -> str:
        return self._p




