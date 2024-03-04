from mdp_policy_iter import convert_policy_to_path, transition
from pyamaze import maze,COLOR,agent
import queue

m=maze()
m.CreateMaze(loadMaze='10x10maze.csv', theme=COLOR.light)
def value_iteration(m, discount_factor=0.99, theta=0.1):
    states = [(i, j) for i in range(1, m.rows+1) for j in range(1, m.cols+1)]
    V = {s: 0 for s in states}  
    rewards = {s: -1 for s in states}  
    rewards[(1, 1)] = 100 

    while True:
        delta = 0
        for s in states:
            v = V[s]
            
            V[s] = max(sum([rewards[s] + discount_factor * V[transition(s, a, m)]]) for a in ['N', 'E', 'S', 'W'])
            delta = max(delta, abs(v - V[s]))
        if delta < theta: 
            break

   
    policy = {}
    for s in states:
        action_values = {}
        for a in ['N', 'E', 'S', 'W']:
            action_values[a] = sum([rewards[s] + discount_factor * V[transition(s, a, m)]])
        policy[s] = max(action_values, key=action_values.get)

    return policy

optimal_policy = value_iteration(m)


path = convert_policy_to_path(m, optimal_policy)


a = agent(m, footprints=True)
m.tracePath({a:path})
m.run()