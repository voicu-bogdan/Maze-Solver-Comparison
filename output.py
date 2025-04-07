fileName = "./Output.txt"

def writeOutput(output):
    file = open(fileName, "w")
    file.write(output)
    file.close()

def clearOutput():
    writeOutput("")

def addOutput(output):
    current = readOutput()
    current.append(output)
    writeOutput("\n".join(current))

def readOutput():
    try:
        with open(fileName, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

def printLabyrinth(labyrinth):
    empty, wall, path = 0, 1, 3
    for row in labyrinth:
        for tile in row:
            if tile == empty:
                print("■", end=" ")
            elif tile == wall:
                print("□", end=" ")
            elif tile == path:
                print("▩", end=" ")
        print()