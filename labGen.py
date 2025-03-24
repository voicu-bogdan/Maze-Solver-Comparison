import numpy as np

def generateLabyrinth(size, percentage):
    labyrinth = np.zeros((size, size)) 
    empty = 0
    wall = 1
    percentage = size * size * percentage * 0.01
    current_percentage = 0
    while current_percentage < percentage:
        x = np.random.randint(0, size)
        y = np.random.randint(0, size)
        if (labyrinth[x][y] == empty) and not((x == 0 and y == 0) or (x==size-1 and y== size-1)): # entrance and exit will be top left and bottom right respectively
            labyrinth[x][y] = wall
            current_percentage+=1
    return(labyrinth) 