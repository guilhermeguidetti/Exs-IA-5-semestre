import numpy as np

class Matrix():
    def __init__(self, m: list):
        self.__matrix = m
        self.movements = list()
        self.size = len(self.__matrix)

    def __str__(self) -> str:
        return str(np.array(self.__matrix))

    def __eq__(self, __o: object) -> bool:
        return self.__matrix == __o.__matrix

    def rotate(self, row: int):
        if row >= 1 and row <= len(self.__matrix):
            selected_row = self.__matrix[row - 1]
            item = selected_row.pop()
            selected_row.insert(0, item)
            self.__matrix[row - 1] = selected_row
            self.movements.append("R" + str(row))

    def undo(self, row: int):
        if row >= 1 and row <= len(self.__matrix):
            selected_row = self.__matrix[row - 1]
            item = selected_row.pop(0)
            selected_row.append(item)
            self.__matrix[row - 1] = selected_row
            self.movements.pop()

    def get_movements(self):
        ret = ""
        for i in range(len(self.movements)):
            ret = ret + self.movements[i]
            if i < len(self.movements) - 1:
                ret = ret + ", "
        return ret
