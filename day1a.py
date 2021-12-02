with open('day1.input', 'r') as f:
    input = [int(x) for x in f.read().split()]

positive_changes = -1 # this is the starting point to account for no initial starting depth.
last_item = 0
for current_item in input:
    if current_item > last_item:
        positive_changes += 1
    last_item = current_item

print(positive_changes)