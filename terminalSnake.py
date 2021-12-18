import random

print("hi")
board_size = int(input("Input number of cells on one side: "))
print(board_size**2)

possible_actions = ["north", "south", "east", "west", "", "quit"]

active_cells = [(0,0)]
direction = "east"
action = ""

def add_tuple(a,b):
    lst = list(a)
    for i in range(len(lst)):
        lst[i] += b[i]
    return tuple(lst)

def make_dot():
    dot = (random.randint(0,board_size-1),random.randint(0,board_size-1))
    while(dot in active_cells):
        dot = (random.randint(0,board_size-1),random.randint(0,board_size-1))
    return dot

hist1 = (0,1)
hist2 = (0,2)

dot = make_dot()
#dot = (active_cells[0][0] + 2, 0)

#Main Gameplay Loop
while action != "quit":
    print("\n\nbegin loop")
    print("Current active cells: " + str(active_cells))
    print("Dot: " + str(dot))

    #get user input
    while True:
        action = input("What do? ")
        if action == "":
            break
        elif action not in possible_actions:
            print("Please try again")
            print(action)
            continue
        else:
            direction = action
            break

    #Store current cells
    hist2 = hist1
    hist1 = active_cells[-1]

    # Execute move;
    # First, "shift" all cells right one
    for i in reversed(range(len(active_cells) - 1)):
        active_cells[i+1] = active_cells[i]

    # Then, change value of [0] cell
    if direction == "east":
        active_cells[0] = add_tuple(active_cells[0], (1,0))
    elif direction == "west":
        active_cells[0] = add_tuple(active_cells[0], (-1, 0))
    elif direction == "north":
        active_cells[0] = add_tuple(active_cells[0], (0, 1))
    elif direction == "south":
        active_cells[0] = add_tuple(active_cells[0], (0, -1))

    if active_cells[0] == dot:
        active_cells.append(hist1)
        hist1 = hist2
        dot = make_dot()
        #dot = (active_cells[0][0] + 2, 0)

    tail = active_cells[1:]
    if active_cells[0] in tail:
        print("BANG! Game over")
        action = "quit"