with open('day1.input', 'r') as f:
    input = [int(x) for x in f.read().split()]

positive_changes = -1 # this is the starting point to account for no initial starting depth.

i = 0
last_sum = 0
while i<len(input)-2: # accounting for the last three-point average ending before the end of the list is reached
    current_sum = input[i]+input[i+1]+input[i+2]
    if current_sum>last_sum:
        positive_changes += 1
    last_sum = current_sum
    i += 1


print(positive_changes)