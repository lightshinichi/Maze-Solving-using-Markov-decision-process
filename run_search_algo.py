import argparse
from pyamaze import maze,agent,COLOR
from search_algo import bfs, dfs, aStarSearch

def run_search_algorithm(algo_name, maze_file):
    m = maze()
    m.CreateMaze(loadMaze=maze_file)
    
    if algo_name.lower() == 'bfs':
        route, time_taken = bfs(m)
        a=agent(m,shape='arrow',footprints=True,color=COLOR.red)

    elif algo_name.lower() == 'dfs':
        route, time_taken = dfs(m)
        a=agent(m,shape='arrow',footprints=True,color=COLOR.blue)
    elif algo_name.lower() == 'astar':
        route, time_taken = aStarSearch(m)
        a=agent(m,footprints=True)
    else:
        raise ValueError("Invalid.")
    print(f"Algorithm: {algo_name.upper()}, Maze: {maze_file}, Time Taken: {time_taken:}s, Steps taken: {len(route)}")
    m.tracePath({a:route})
    m.run()
   


parser = argparse.ArgumentParser()
parser.add_argument("algorithm")
parser.add_argument("maze_file")

args = parser.parse_args()

run_search_algorithm(args.algorithm, args.maze_file)
