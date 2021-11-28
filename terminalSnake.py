import random

print("hi")
board_size = int(input("Input number of cells on one side: "))
print(board_size**2)

possible_actions = ["north", "south", "east", "west", "", "quit"]

num_active = 1
cell_history = [[0,1]]
active_cells = [[0,0]]
last_cell = [-1,0]
direction = "east"
vector = [1,0]
action = ""

def make_dot():
    dot = [random.randint(0,board_size-1),random.randint(0,board_size-1)]
    while(dot in active_cells):
        dot = [random.randint(0,board_size-1),random.randint(0,board_size-1)]
    return dot

def add_vect(a = [], b = []):
    a[0] += b[0]
    a[1] += b[1]
    return a

def store_cells():
    for i in range(len(active_cells)):
        cell_history[i][0] = active_cells[i][0]
        cell_history[i][1] = active_cells[i][1]

dot = make_dot()

def store_cell():
    last_cell[0] = active_cells[-1][0]
    last_cell[1] = active_cells[-1][1]
    print("Stored; last cell = " + str(last_cell))

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

    #Store current cell
    store_cell()
    #print("Type: " + str(type(active_cells[0][0])))

    # Execute move;
    # First, "shift" all cells right one
    for i in range(len(active_cells) - 1):
        active_cells[i+1] = active_cells[i]
    # Then, change value of [0] cell
    if direction == "east":
        active_cells[0][0] += 1
    elif direction == "west":
        active_cells[0][0] -= 1
    elif direction == "north":
        active_cells[0][1] += 1
    elif direction == "south":
        active_cells[0][1] -= 1

    #print("cell_history: " + str(cell_history))

    if active_cells[0] == dot:
        #print("cell history 2: " + str(cell_history))
        active_cells.append(last_cell)
        #cell_history.append(active_cells[0])
        dot = make_dot()