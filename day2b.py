import numpy as np

def convert_to_vector(direction, X, current_aim):
    if direction == "forward":
         # increase horizontal by X, increase depth by current aim * X
        return np.array([X,current_aim*X,0])
    if direction == "down":
        # increase aim by X
        return np.array([0,0,X]) 
    if direction == "up":
        # decrease aim by X
        return np.array([0,0,-1*X]) 

# position vector is now (horisontal, depth, aim)
position = np.array([0,0,0])
with open('day2.input', 'r') as f:
    for line in f:
        line_split = line.split(' ')
        position_change = convert_to_vector(line_split[0], int(line_split[1]), position[2])
        position += position_change

print(position[0]*position[1])

        

