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
hist3 = (0,3)

#dot = make_dot()
dot = (active_cells[0][0] + 2, 0)

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
    hist3 = hist2
    hist2 = hist1
    print(hist1)
    hist1 = active_cells[-1]
    #store_cell()

    # Execute move;
    # First, "shift" all cells right one
    for i in reversed(range(len(active_cells) - 1)):
        active_cells[i+1] = active_cells[i]

    # Then, change value of [0] cell
    if direction == "east":
        #active_cells[0][0] += 1
        active_cells[0] = add_tuple(active_cells[0], (1,0))
    elif direction == "west":
        #active_cells[0][0] -= 1
        active_cells[0] = add_tuple(active_cells[0], (-1, 0))
    elif direction == "north":
        #active_cells[0][1] += 1
        active_cells[0] = add_tuple(active_cells[0], (0, 1))
    elif direction == "south":
        #active_cells[0][1] -= 1
        active_cells[0] = add_tuple(active_cells[0], (0, -1))

    #print("cell_history: " + str(cell_history))

    if active_cells[0] == dot:
        #print("cell history 2: " + str(cell_history))
        active_cells.append(hist1)
        hist1 = hist2
        hist2 = hist3
        #dot = make_dot()
        dot = (active_cells[0][0] + 2, 0)