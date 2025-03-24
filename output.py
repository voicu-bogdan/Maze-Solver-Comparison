fileName = "./Output.txt"
def writeOutput(output):
    file = open(fileName, "w")
    file.write(output)
    file.close()

def clearOutput():
    writeOutput("")

def addOutput(output):
    pass

def readOutput():
    pass

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