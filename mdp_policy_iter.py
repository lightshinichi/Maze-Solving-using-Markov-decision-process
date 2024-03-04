from pyamaze import maze, agent, COLOR
import numpy as np

def initialize_mdp(m):
    states = [(i, j) for i in range(1, m.rows+1) for j in range(1, m.cols+1)]
    actions = ['N', 'S', 'E', 'W']
    rewards = {s: -1 for s in states}
    rewards[(1, 1)] = 100
    policy = {s: np.random.choice(actions) for s in states}
    return states, actions, rewards, policy

def policy_evaluation(policy, states, rewards, m, discount_factor=0.99, theta=0.1):
    V = {s: 0 for s in states}
    while True:
        delta = 0
        for s in states:
            v = V[s]
            a = policy[s]
            V[s] = sum([rewards[s] + discount_factor * V[transition(s, a, m)]])
            delta = max(delta, abs(v - V[s]))
        if delta < theta:
            break
    return V

def policy_improvement(V, policy, states, actions, rewards, m, discount_factor=0.99):
    policy_stable = True
    for s in states:
        old_action = policy[s]
        action_values = {}
        for a in actions:
            action_values[a] = sum([rewards[s] + discount_factor * V[transition(s, a, m)]])
        best_action = max(action_values, key=action_values.get)
        policy[s] = best_action
        if old_action != best_action:
            policy_stable = False
    return policy, policy_stable

def transition(state, action, m):
    if m.maze_map[state][action]:
        if action == 'N':
            return (state[0]-1, state[1])
        if action == 'S':
            return (state[0]+1, state[1])
        if action == 'E':
            return (state[0], state[1]+1)
        if action == 'W':
            return (state[0], state[1]-1)
    return state

def policy_iteration(m):
    states, actions, rewards, policy = initialize_mdp(m)
    while True:
        V = policy_evaluation(policy, states, rewards, m)
        policy, policy_stable = policy_improvement(V, policy, states, actions, rewards, m)
        if policy_stable:
            return policy

def convert_policy_to_path(m, policy):
    start = (m.rows, m.cols)
    goal = (1, 1)
    current_state = start
    path = []
    while current_state != goal:
        action = policy[current_state]
        path.append(current_state)
        if action == 'N':
            next_state = (current_state[0]-1, current_state[1])
        elif action == 'S':
            next_state = (current_state[0]+1, current_state[1])
        elif action == 'E':
            next_state = (current_state[0], current_state[1]+1)
        elif action == 'W':
            next_state = (current_state[0], current_state[1]-1)
        current_state = next_state
    path.append(goal)
    path_dict = {}
    for i in range(len(path)-1):
        path_dict[path[i]] = path[i+1]
    return path_dict

if __name__ == '__main__':
    m = maze()
    m.CreateMaze(loadMaze='10x10maze.csv', theme=COLOR.light)
    optimal_policy = policy_iteration(m)
    path = convert_policy_to_path(m, optimal_policy)
    a = agent(m, footprints=True)
    m.tracePath({a:path})
    m.run()
