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
    for row in labyrinth:
        for tile in row:
            if tile == 0:
                print("■", end=" ")
            elif tile == 1:
                print("□", end=" ")
        print()