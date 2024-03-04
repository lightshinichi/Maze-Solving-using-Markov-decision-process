import argparse
import time
import matplotlib.pyplot as plt
from pyamaze import maze, agent, COLOR
from mdp_policy_iter import policy_iteration, convert_policy_to_path, transition  # Assuming similar structure
from mdp_value_iter import value_iteration  

def run_iteration(maze_file, iteration_func, plot_choice):
    m = maze()
    m.CreateMaze(loadMaze=maze_file, theme=COLOR.light)
    start_time = time.time()
    optimal_policy = iteration_func(m)
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    if plot_choice == 'time':
        return elapsed_time
    elif plot_choice == 'steps':
        path = convert_policy_to_path(m, optimal_policy)
        return len(path)  
    else:
        print("Invalid plot choice.")
        return None

def compare_mdp(plot_choice):
    maze_files = ['10x10maze.csv', '20x20maze.csv', '30x30maze.csv']  
    times_or_steps = []
    
    for maze_file in maze_files:
        result = run_iteration(maze_file, policy_iteration, plot_choice)  # Comment if needed
        # result = run_iteration(maze_file, value_iteration, plot_choice) 
        times_or_steps.append(result)
    
    plt.figure(figsize=(10, 6))
    plt.plot(maze_files, times_or_steps, marker='o', linestyle='-', color='b')
    plt.title(f'Maze Iteration {plot_choice.capitalize()}')
    plt.xlabel('Maze Size')
    plt.ylabel(f'{plot_choice.capitalize()}')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()


parser = argparse.ArgumentParser(description="Plot time or steps for maze solving algorithms.")
parser.add_argument('choice', choices=['time', 'steps'], help="Choose what to plot: 'time' or 'steps'")
args = parser.parse_args()

compare_mdp(args.choice)
