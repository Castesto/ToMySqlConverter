import datetime as dt


class CheckType:

    __TYPE = ["string", "float", "int", "datetime", "nan"]
    __p = "none"

    def __init__(self, argument):
        print("инициализируем")
        if argument == self.__TYPE[4]:
            self.__p = self.__TYPE[4]
        elif self.__is_date(argument):
            self.__p = self.__TYPE[3]
        elif self.__is_int(argument):
            self.__p = self.__TYPE[2]
        elif self.__is_float(argument):
            self.__p = self.__TYPE[1]
        elif self.__is_string(argument):
            self.__p = self.__TYPE[0]
        else:
            self.__p = "No matches"

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
            date_formatter = "%d-%m-%Y %H:%M:%S"
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
        return self.__p




