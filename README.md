# Maze Solver and MDP Algorithms

## Table of Contents

- [Introduction](#introduction)
- [Running the Search Algorithms](#running-the-search-algorithms)
- [Running the MDP Algorithms](#running-the-mdp-algorithms)
- [Visualizing Comparison Graphs](#visualizing-comparison-graphs)

## Introduction

This project includes implementations of various search algorithms and Markov Decision Process (MDP) algorithms to solve mazes. The search algorithms include Depth First Search (DFS) and A* (A-star), while the MDP algorithms include policy iteration and value iteration.

## Running the Search Algorithms

To run the search algorithm, use the following command in the terminal:

```bash
python run_search_algo.py --algo --maze.csv

eg: python run_search_algo.py dfs 10x10maze.csv
    python run_search_algo.py astar 30x30maze.csv

To run the MDP algorithm, use( The size of the maze can be changed here (m.CreateMaze(loadMaze='10x10maze.csv', theme=COLOR.light) )

python .\mdp_policy_iter.py # for policy iteration
python .\mdp_value_iter.py # for Value iteration

To visualize the comparsion graph for search algo, use the following

python compare.py --algo dfs --metric steps #for steps
python compare.py --algo bfs --metric time #time consumed

To visualize the comparsion graph for MDP algo (Change the value or policy iteration by commenting this line result = run_iteration(maze_file, policy_iteration, plot_choice)  and uncommenting the other line ), use the following

python compare_mdp.py time 
python compare_mdp.py step 
