import numpy as np
import pylab as plt

# map cell to cell, add circular cell to goal point
#points_list = [(0,1), (0,2), (0,3), (1,4), (1,5), (4,10), (4,11), (5,12), (5,13), (2,6), (2,7), (3,8), (3,9)]
#points_list = [(0,1), (0,2), (0,3), (1,4), (1,5), (4,9), (4,10), (5,9), (5,11), (2,6), (2,7), (6,9), (6,12),(7,9), (7,13), (3,9), (3,8)]

p1 = 1
p2 = 2
p3 = 3
auto = 9
cabra1 = 10
cabra2 = 11

#points_list = [(0,'p1'), (0,'p2'), (0,'p3'), ('p1',4), ('p1',5), (4,9), (4,10), (5,9), (5,11), ('p2',6),
#               ('p2',7), (6,9), (6,12),(7,9), (7,13), ('p3',9), ('p3',8)]

#points_list = [(0,p1), (0,p2), (0,p3), (p1,4), (p1,5), (4,9), (4,10), (5,9), (5,11), (p2,6),
#               (p2,7), (6,9), (6,12),(7,9), (7,13), (p3,9), (p3,8)]

#version ZZZ
##points_list = [(0,p1), (0,p2), (0,p3),
##               (p1,4), (4,auto), (4,10), (p1,5),(5,auto), (5,11),
##               (p2,6), (6,auto), (6,12), (p2,7) ,(7,auto), (7,13),
##               (p3,auto), (p3,8)]

points_list = [(0,p1), (0,p2), (0,p3),
               (p1,4), (4,auto), (4,cabra1), (p1,5),(5,auto), (5,cabra2),
               (p2,6), (6,auto), (6,cabra1), (p2,7) ,(7,auto), (7,cabra2),
               (p3,auto), (p3,8)]

goal = auto

import networkx as nx
G=nx.Graph()
G.add_edges_from(points_list)
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G,pos)
nx.draw_networkx_edges(G,pos)
nx.draw_networkx_labels(G,pos)
plt.show()

points_list2 = [(0,'p1'), (0,'p2'), (0,'p3'),
               ('p1',4), (4,'auto'), (4,'cabra1'), ('p1',5),(5,'auto'), (5,'cabra2'),
               ('p2',6), (6,'auto'), (6,'cabra1'), ('p2',7) ,(7,'auto'), (7,'cabra2'),
               ('p3','auto'), ('p3',8)]

import networkx as nx2
G2=nx2.Graph()
G2.add_edges_from(points_list2)
pos2 = nx.spring_layout(G2)
nx2.draw_networkx_nodes(G2,pos2)
nx2.draw_networkx_edges(G2,pos2)
nx2.draw_networkx_labels(G2,pos2)
plt.show()

# how many points in graph? x points
MATRIX_SIZE = 12 #14 con version ZZZ

# create matrix x*y
R = np.matrix(np.ones(shape=(MATRIX_SIZE, MATRIX_SIZE)))
R *= -1

# assign zeros to paths and 100 to goal-reaching point
for point in points_list:
    print(point)
    if point[1] == goal:
        R[point] = 100
    else:
        R[point] = 0

    if point[0] == goal:
        R[point[::-1]] = 100
    else:
        # reverse of point
        R[point[::-1]]= 0

# add goal point round trip
R[goal,goal]= 100

R

##matrix([[  -1.,    0.,   -1.,   -1.,   -1.,   -1.,   -1.,   -1.],
##        [   0.,   -1.,    0.,   -1.,   -1.,    0.,   -1.,   -1.],
##        [  -1.,    0.,   -1.,    0.,   -1.,   -1.,   -1.,  100.],
##        [  -1.,   -1.,    0.,   -1.,   -1.,   -1.,   -1.,   -1.],
##        [  -1.,   -1.,   -1.,   -1.,   -1.,    0.,   -1.,   -1.],
##        [  -1.,    0.,   -1.,   -1.,    0.,   -1.,    0.,   -1.],
##        [  -1.,   -1.,   -1.,   -1.,   -1.,    0.,   -1.,   -1.],
##        [  -1.,   -1.,    0.,   -1.,   -1.,   -1.,   -1.,  100.]])

Q = np.matrix(np.zeros([MATRIX_SIZE,MATRIX_SIZE]))

# learning parameter
gamma = 0.8

initial_state = 1

def available_actions(state):
    current_state_row = R[state,]
    av_act = np.where(current_state_row >= 0)[1]
    return av_act

available_act = available_actions(initial_state) 

def sample_next_action(available_actions_range):
    next_action = int(np.random.choice(available_act,1))
    return next_action

action = sample_next_action(available_act)

def update(current_state, action, gamma):
    
  max_index = np.where(Q[action,] == np.max(Q[action,]))[1]
  
  if max_index.shape[0] > 1:
      max_index = int(np.random.choice(max_index, size = 1))
  else:
      max_index = int(max_index)
  max_value = Q[action, max_index]
  
  Q[current_state, action] = R[current_state, action] + gamma * max_value
  print('max_value', R[current_state, action] + gamma * max_value)
  
  if (np.max(Q) > 0):
    return(np.sum(Q/np.max(Q)*100))
  else:
    return (0)
    
update(initial_state, action, gamma)

# Training
scores = []
for i in range(300):
    current_state = np.random.randint(0, int(Q.shape[0]))
    available_act = available_actions(current_state)
    action = sample_next_action(available_act)
    score = update(current_state,action,gamma)
    scores.append(score)
    print ('Score:', str(score))
    
print("Trained Q matrix:")
print(Q/np.max(Q)*100)

# Testing
current_state = 0
steps = [current_state]

while current_state != goal:

    next_step_index = np.where(Q[current_state,] == np.max(Q[current_state,]))[1]
    
    if next_step_index.shape[0] > 1:
        next_step_index = int(np.random.choice(next_step_index, size = 1))
    else:
        next_step_index = int(next_step_index)
    
    steps.append(next_step_index)
    current_state = next_step_index

print("Most efficient path:")
print(steps)

plt.plot(scores)
plt.show()

#Most efficient path:
#[0, 3, 9]
