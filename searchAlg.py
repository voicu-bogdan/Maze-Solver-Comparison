import heapq

def heuristic(current_position, goal_position):
    return abs(current_position[0]-goal_position[0]) + abs(current_position[1]-goal_position[1])

def aStar(labyrinth):
    labyrinth_size = len(labyrinth)
    empty, wall, path, head = 0, 1, 2, 3
    start, goal = (0, 0), (labyrinth_size-1, labyrinth_size-1)
    
    open_set = []
    heapq.heappush(open_set, (heuristic(start, goal), 0, start, [start]))
    
    visited = set()
    visited_count = 0
    came_from = {}
    g_scores = {start: 0}
    f_scores = {start: heuristic(start, goal)}
    
    while open_set:
        _, current_g, current_pos, path = heapq.heappop(open_set)
        
        if current_pos == goal:
            return path, visited_count
        
        if current_pos in visited:
            continue
            
        visited.add(current_pos)
        visited_count += 1
        
        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            neighbor = (current_pos[0]+dx, current_pos[1]+dy)
            
            if (0 <= neighbor[0] < labyrinth_size and 
                0 <= neighbor[1] < labyrinth_size and 
                labyrinth[neighbor[0]][neighbor[1]] != wall):
                
                tentative_g = current_g + 1
                
                if neighbor not in g_scores or tentative_g < g_scores[neighbor]:
                    came_from[neighbor] = current_pos
                    g_scores[neighbor] = tentative_g
                    f_scores[neighbor] = tentative_g + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_scores[neighbor], tentative_g, neighbor, path + [neighbor]))
    
    return None, visited_count

def uniformCost(labyrinth):
    labyrinth_size = len(labyrinth)
    empty, wall, path, head = 0, 1, 2, 3
    start, goal = (0, 0), (labyrinth_size-1, labyrinth_size-1)
    
    open_set = []
    heapq.heappush(open_set, (0, start, [start]))
    
    visited = set()
    visited_count = 0
    
    while open_set:
        current_cost, current_pos, path = heapq.heappop(open_set)
        
        if current_pos == goal:
            return path, visited_count
            
        if current_pos in visited:
            continue
            
        visited.add(current_pos)
        visited_count += 1
        
        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            neighbor = (current_pos[0]+dx, current_pos[1]+dy)
            
            if (0 <= neighbor[0] < labyrinth_size and 
                0 <= neighbor[1] < labyrinth_size and 
                labyrinth[neighbor[0]][neighbor[1]] != wall):
                
                new_cost = current_cost + 1
                heapq.heappush(open_set, (new_cost, neighbor, path + [neighbor]))
    
    return None, visited_count