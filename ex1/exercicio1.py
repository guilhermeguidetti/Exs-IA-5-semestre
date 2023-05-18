# Henrique Vergili - 21005466
# Guilherme Guidetti - 21001718
# Leonardo Hana - 20124988

from copy import deepcopy
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

def findAnswer(start: Matrix, objective: Matrix):
    tries = 0
    states = [start]
    explored_cases = [deepcopy(states[0])]
    while len(states) > 0:
        tries = tries + 1
        if states[0] == objective:
            return {
                "movements": states[0].get_movements(),
                "tries": tries,
            }
        for substate in range(states[0].size):
            states[0].rotate(substate + 1)
            try:
                explored_cases.index(states[0])
            except:
                states.append(deepcopy(states[0]))
                explored_cases.append(deepcopy(states[0]))
            states[0].undo(substate + 1)
        states.pop(0)
    return {
        "movements": "Impossível",
        "tries": tries,
    }

option = "n"
while option == "n":
    start = list()
    objective = list()
    for type in range(2):
        if type == 0:
            print("Digite a matriz do estado inicial separada por espaços e quebrando as linhas: ")
        else:
            print("Digite a matriz do estado desejado separada por espaços e quebrando as linhas: ")
        for i in range(3):
            elements = list(map(str, input().split()))
            if type == 0:
                start.append(elements)
            else:
                objective.append(elements)
    print("Estas duas matrizes estão corretas?")
    print("Matriz Estado Inicial")
    print(np.array(start))
    print("Matriz Estado Desejado")
    print(np.array(objective))
    option = ""
    while option != "s" and option != "n":
        option = input("s/n: ")
result = findAnswer(Matrix(start), Matrix(objective))
print("\nResultados:")
print(result["movements"])
print(result["tries"])
