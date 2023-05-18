from matrix import Matrix
from copy import deepcopy
import numpy as np

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