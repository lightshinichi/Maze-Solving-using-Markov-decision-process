from pyamaze import maze, agent, COLOR
import numpy as np
from mdp_policy_iter import policy_iteration, convert_policy_to_path
from mdp_value_iter import value_iteration


m = maze(10,10)

m.CreateMaze( theme=COLOR.light)
optimal_policy = policy_iteration(m) #Uncomment based on need
# optimal_policy = value_iteration(m)

path = convert_policy_to_path(m, optimal_policy)


a = agent(m, footprints=True)
m.tracePath({a:path})
m.run()

