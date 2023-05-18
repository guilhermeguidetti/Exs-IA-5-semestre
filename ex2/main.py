import random
from prettytable import PrettyTable


class Ambient:
    def __init__(self, dirty, present, name):
        self.dirty = dirty
        self.vacuum_present = present
        self.name = name

    def __str__(self):
        return f"{self.name} Está sujo: {self.dirty} Robo limpando: {self.vacuum_present}"


def generateAmbient(rooms: int, dirty_rooms: int):
    if not (0 < rooms <= 10):
        raise ValueError("Número de salas deve ser entre 1 e 10.")
    if not (0 <= dirty_rooms <= rooms):
        raise ValueError("Número de salas sujas deve ser entre 0 e o número de salas.")

    ambients = list()
    presence_pos = random.randint(0, rooms - 1)
    room_names = list(map(chr, range(ord('A'), ord('A') + rooms)))
    d = list()
    for j in range(rooms):
        if j < dirty_rooms:
            d.append(True)
        else:
            d.append(False)
    random.shuffle(d)
    for i in range(rooms):
        ambients.append(Ambient(d[i], False, room_names[i]))
        if i == presence_pos:
            ambients[i].vacuum_present = True
    return ambients


def printAmbientTotal(ambient):
    print("\nAmbiente Observável")
    table = PrettyTable()
    table.add_column("Sala", ['Sujo', 'Robo'])
    for i in range(n_rooms):
        presence = "" if ambient[i].vacuum_present == False else "X"
        dirty = "X" if ambient[i].dirty == True else ""
        table.add_column(ambient[i].name, [dirty, presence])
    print(table)


def printAmbientPartial(ambient):
    print("\nAmbiente Parcialmente Observável")
    table = PrettyTable()
    table.add_column("Sala", ['Sujo', 'Robo'])
    for i in range(n_rooms):
        if not ambient[i].vacuum_present:
            dirty = "?"
        else:
            dirty = "X" if ambient[i].dirty == True else ""
        presence = "" if ambient[i].vacuum_present == False else "X"
        table.add_column(ambient[i].name, [dirty, presence])
    print(table)


def printAmbient(ambient, onicient):
    if onicient == 'S':
        printAmbientTotal(ambient)
    elif onicient == 'N':
        printAmbientPartial(ambient)


def clean(ambient):
    if ambient.dirty == False:
        print("Ambiente já está limpo!")
    else:
        ambient.dirty = False
        print("Ambiente foi limpo!")


def getCurrentRoom(ambient):
    for i in range(len(ambient)):
        if not ambient[i].vacuum_present:
            continue
        else:
            return i


def manualControl(ambient, onicient):
    printAmbient(ambient, onicient)
    while True:
        current_room = getCurrentRoom(ambient)

        print(f"\nAspirador está na sala: {ambient[current_room].name}")
        action = input(
            "Escolha uma ação (digite 'e' para mover para esquerda, 'd' para mover para direita, 'l' para limpar ou 's' para sair): ").upper()

        if action == "E" and current_room != 0:
            ambient[current_room].vacuum_present = False
            ambient[current_room - 1].vacuum_present = True

        elif action == "D" and current_room != n_rooms - 1:
            ambient[current_room].vacuum_present = False
            ambient[current_room + 1].vacuum_present = True

        elif action == "L":
            clean(ambient[current_room])

        elif action == "S":
            break
        printAmbient(ambient, onicient)

def automaticControl(ambient, oniscient):
    printAmbient(ambient, oniscient)
    if oniscient == "S":
        dirty_rooms = n_dirty_rooms
        while dirty_rooms != 0:
            closest_dist = 10
            closest_room = -1
            for i in range(n_rooms):
                if ambient[i].dirty and abs(getCurrentRoom(ambient) - i) < closest_dist:
                    closest_dist = abs(getCurrentRoom(ambient) - i)
                    closest_room = i;
            if closest_room == -1:
                print("Tudo limpo!")
            else:
                current_room = getCurrentRoom(ambient)
                while current_room != closest_room:
                    if closest_room - current_room > 0:
                        ambient[current_room].vacuum_present = False
                        ambient[current_room + 1].vacuum_present = True
                        current_room += 1
                    else:
                        ambient[current_room].vacuum_present = False
                        ambient[current_room - 1].vacuum_present = True
                        current_room -= 1
                    printAmbient(ambient, oniscient)
                clean(ambient[current_room])
                dirty_rooms -= 1
        printAmbient(ambient, oniscient)
    elif oniscient == "N":
        if getCurrentRoom(ambient) >= n_rooms / 2:
            preffered_direction = "D"
        else:
            preffered_direction = "E"
        explored_areas = list()
        for i in range(n_rooms):
            explored_areas.append(False)
        while False in explored_areas:
            current = getCurrentRoom(ambient)
            clean(ambient[current])
            explored_areas[current] = True
            if preffered_direction == "D" and current != n_rooms - 1:
                ambient[current].vacuum_present = False
                ambient[current + 1].vacuum_present = True
            elif preffered_direction == "E" and current != 0:
                ambient[current].vacuum_present = False
                ambient[current - 1].vacuum_present = True
            elif current == n_rooms - 1:
                preffered_direction = "E"
                ambient[current].vacuum_present = False
                ambient[current - 1].vacuum_present = True
            elif current == 0:
                preffered_direction = "D"
                ambient[current].vacuum_present = False
                ambient[current + 1].vacuum_present = True
            printAmbient(ambient, oniscient)

while True:
    try:
        n_rooms = int(input('Digite o numero de salas: '))
        n_dirty_rooms = int(input('Digite o numero de salas sujas: '))
        ia_based = input('Utilizar I.A.? (S/N): ').upper()
        a = generateAmbient(n_rooms, n_dirty_rooms)
        if ia_based == 'S':
            is_onicient = input('Ambiente será onisciente? (S/N): ').upper()
            if is_onicient == 'S' or 'N':
                automaticControl(a, is_onicient)
        elif ia_based == 'N':
            is_onicient = input('Ambiente será onisciente? (S/N): ').upper()
            if is_onicient == 'S' or 'N':
                manualControl(a, is_onicient)
    except ValueError as e:
        print(e)