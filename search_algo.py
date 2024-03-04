from pyamaze import maze,COLOR,agent
import time
from queue import PriorityQueue

def dfs(maze):
    start_time = time.perf_counter()  

    entry = (maze.rows, maze.cols)
    visited = [entry]
    stack = [entry]
    path = {}
    traversalPath = [entry]
    steps = 0  

    while stack:
        current = stack.pop()
        traversalPath.append(current)
        steps += 1  
        
        if current == (1, 1):
            break

        for direction in 'ESNW':
            if maze.maze_map[current][direction]:
                if direction == 'E':
                    next_cell = (current[0], current[1] + 1)
                elif direction == 'W':
                    next_cell = (current[0], current[1] - 1)
                elif direction == 'S':
                    next_cell = (current[0] + 1, current[1])
                else:  # 'N'
                    next_cell = (current[0] - 1, current[1])

                if next_cell in visited:
                    continue

                visited.append(next_cell)
                stack.append(next_cell)
                path[next_cell] = current

    route = {}
    cell = (1, 1)
    while cell != entry:
        route[path[cell]] = cell
        cell = path[cell]

    
    elapsed_time = time.perf_counter() - start_time
    

    return route, elapsed_time

def bfs(maze):
    start_time = time.perf_counter()
    start_position = (maze.rows, maze.cols)
    queue = [start_position]
    visited = set([start_position])
    path_to_follow = {}
    
    steps = 0
    while queue:
        current_position = queue.pop(0)
        steps +=1

        if current_position == (1, 1):
            break
        
        for direction in 'ESNW':
            if maze.maze_map[current_position][direction]:
                if direction == 'E':
                    next_position = (current_position[0], current_position[1]+1)
                elif direction == 'W':
                    next_position = (current_position[0], current_position[1]-1)
                elif direction == 'N':
                    next_position = (current_position[0]-1, current_position[1])
                else:  # 'S'
                    next_position = (current_position[0]+1, current_position[1])
                
                if next_position in visited:
                    continue
                
                queue.append(next_position)
                visited.add(next_position)
                path_to_follow[next_position] = current_position
    
    route = {}
    current_cell = (1, 1)
    while current_cell != start_position:
        route[path_to_follow[current_cell]] = current_cell
        current_cell = path_to_follow[current_cell]
    elapsed_time = time.perf_counter() - start_time
    return route, elapsed_time





def heuristic(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x1 - x2) + abs(y1 - y2)

def aStarSearch(maze):
    start_time = time.perf_counter()  

    start_position = (maze.rows, maze.cols)
    goal_position = (1, 1)
    
    g_scores = {cell: float('inf') for cell in maze.grid}
    g_scores[start_position] = 0
    
    f_scores = {cell: float('inf') for cell in maze.grid}
    f_scores[start_position] = heuristic(start_position, goal_position)
    
    open_set = PriorityQueue()
    open_set.put((f_scores[start_position], heuristic(start_position, goal_position), start_position))
    
    path_tracker = {}
    
    while not open_set.empty():
        current_position = open_set.get()[2]
        
        if current_position == goal_position:
            break
        
        for direction in 'ESNW':
            if maze.maze_map[current_position][direction]:
                if direction == 'E':
                    next_position = (current_position[0], current_position[1] + 1)
                elif direction == 'W':
                    next_position = (current_position[0], current_position[1] - 1)
                elif direction == 'N':
                    next_position = (current_position[0] - 1, current_position[1])
                elif direction == 'S':
                    next_position = (current_position[0] + 1, current_position[1])
                
                tentative_g_score = g_scores[current_position] + 1
                
                if tentative_g_score < g_scores[next_position]:
                    path_tracker[next_position] = current_position
                    g_scores[next_position] = tentative_g_score
                    f_scores[next_position] = tentative_g_score + heuristic(next_position, goal_position)
                    open_set.put((f_scores[next_position], heuristic(next_position, goal_position), next_position))
    
    route = {}
    current_cell = goal_position
    while current_cell != start_position:
        route[path_tracker[current_cell]] = current_cell
        current_cell = path_tracker[current_cell]
    
    
    elapsed_time = time.perf_counter() - start_time

    return route, elapsed_time
