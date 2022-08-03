import datetime as dt


class CheckType:

    __TYPE = ["string", "int", "float", "datetime", "nan"]
    __p = ""

    def __init__(self, argument):
        if argument == self.__TYPE[4]:
            __p = self.__TYPE[4]
        elif self.__is_date(argument):
            __p = self.__TYPE[3]
        elif self.__is_float(argument):
            __p = self.__TYPE[2]
        elif self.__is_int(argument):
            __p = self.__TYPE[1]
        elif self.__is_string(argument):
            __p = self.__TYPE[0]
        else:
            __p = "No matches"

    def __is_int(self, argument):
        try:
            int(argument)
            return True
        except ValueError:
            return False

    def __is_float(self, argument):
        try:
            float(argument)
            return True
        except ValueError:
            return False

    def __is_float_with_fraction(self, argument):
        if self.is_float(argument) and self.is_int(argument):
            if float(argument) - int(argument) == 0:
                return False
            else:
                return True
        else:
            return True

    def __is_date(self, argument):
        try:
            date_formatter = "%d-%m-%Y %H:%M:%S"
            dt.datetime.strptime(argument, date_formatter)
            return True
        except ValueError:
            return False




