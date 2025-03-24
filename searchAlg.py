import heapq

def heuristic(current_position, goal_position):
    # Using manhattan distance
    return abs(current_position[0]-goal_position[0]) + abs(current_position[1]-goal_position[1])

def aStar(labyrinth):
    labyrinth_size = len(labyrinth)
    empty, wall, path, head = 0, 1, 2, 3
    start, goal = (0, 0), (labyrinth_size-1, labyrinth_size-1)
    labyrinth[0][0] = head

    queue = []
    heapq.heappush(open_set, (heuristic(start, goal), 0, start, [start]))

    visited = set()
    visited_count = 0

    came_from = {}
    g_scores = {start: 0}
    f_scores = {start: heuristic(start, goal)}