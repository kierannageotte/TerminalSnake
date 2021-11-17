print("hi")
board_size = int(input("Input number of cells on one side: "))
print(board_size**2)

possible_actions = ["north", "south", "east", "west", "", "quit"]

active_cells = [[0,0]]
direction = "east"
action = ""
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

    if direction == "east":
        active_cells[0][0] += 1
    elif direction == "west":
        active_cells[0][0] -= 1
    elif direction == "north":
        active_cells[0][1] += 1
    elif direction == "south":
        active_cells[0][1] -= 1

    print(active_cells)