import argparse
from search_algo import bfs, dfs, aStarSearch
from pyamaze import maze
import matplotlib.pyplot as plt

def compare():
    parser = argparse.ArgumentParser(description='Compare Maze Solving Algorithms')
    parser.add_argument('--algo', choices=['bfs', 'dfs', 'astar'], required=True, help='Algorithm to use: bfs, dfs, astar')
    parser.add_argument('--metric', choices=['time', 'steps'], required=True, help='Metric to plot: time or steps')
    
    args = parser.parse_args()
    
    times = {'bfs': [], 'dfs': [], 'astar': []}
    steps = {'bfs': [], 'dfs': [], 'astar': []}
    mazes = ['10x10maze.csv', '20x20maze.csv', '30x30maze.csv', '40x40maze.csv']
    m = maze()

    for n in mazes:
        m.CreateMaze(loadMaze=n)
        if args.algo in ['astar']:
            as_route, as_time = aStarSearch(m)
            times['astar'].append(as_time)
            steps['astar'].append(len(as_route))
        if args.algo in ['bfs']:
            bf_route, bfs_time = bfs(m)
            times['bfs'].append(bfs_time)
            steps['bfs'].append(len(bf_route))
        if args.algo in ['dfs']:
            dfs_route, dfs_time = dfs(m)
            times['dfs'].append(dfs_time)
            steps['dfs'].append(len(dfs_route))

    
    maze_sizes = [10, 20, 30, 40]
    
    if args.metric == 'time':
        plt.plot(maze_sizes, times[args.algo], label=args.algo.upper() + ' Time')
        plt.ylabel('Time Taken (ms)')
    elif args.metric == 'steps':
        plt.plot(maze_sizes, steps[args.algo], label=args.algo.upper() + ' Steps')
        plt.ylabel('Steps Taken')

    plt.xlabel('Maze Size')
    plt.title(f'{args.algo.upper()} Algorithm Performance ({args.metric.capitalize()})')
    plt.legend()
    plt.show()

compare()