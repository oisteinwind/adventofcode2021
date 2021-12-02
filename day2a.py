import numpy as np

def convert_to_vector(direction, X):
    if direction == "forward":
        return np.array([X,0]) # increase horizontal by X
    if direction == "down":
        return np.array([0,X]) # increase depth by X
    if direction == "up":
        return np.array([0,-1*X]) # decrease depth by X

# position is (horizontal, depth)
final_position = np.array([0,0])
with open('day2.input', 'r') as f:
    for line in f:
        line_split = line.split(' ')
        position_change = convert_to_vector(line_split[0], int(line_split[1]))
        final_position += position_change

print(final_position[0]*final_position[1])

        

