import random

print("hi")
board_size = int(input("Input number of cells on one side: "))
print(board_size**2)

possible_actions = ["north", "south", "east", "west", "", "quit"]

active_cells = [[0,0]]
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

dot = make_dot()

#Main Gameplay Loop
while action != "quit":
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

    #Execute actions
    if direction == "east":
        active_cells[0][0] += 1
    elif direction == "west":
        active_cells[0][0] -= 1
    elif direction == "north":
        active_cells[0][1] += 1
    elif direction == "south":
        active_cells[0][1] -= 1

#    if active_cells[0] == dot:
#       active_cells +=
    print(active_cells)