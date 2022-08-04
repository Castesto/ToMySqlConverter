class TextReader:
    __text_line_massive: str = []
    __path: str = ""

    def __init__(self, path: str, split_argument: str):
        self.__text_line_massive: str = []
        self.text_reader(path, split_argument)

    def text_reader(self, path: str, split_argument: str):
        file1 = open(path, "r", encoding="utf-8")
        while True:
            line = file1.readline()
            text_line = line.split(split_argument)
            self.__text_line_massive.append(text_line)
            if not line:
                break
        file1.close()

    def get_text_line_massive(self) -> str:
        return self.__text_line_massive
