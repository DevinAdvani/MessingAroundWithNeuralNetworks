import numpy as np

# settings
rows = 10
columns = 10
x = 0
y = 0


# game cycle
while True:
    environment = np.zeros((rows,columns))
    environment[y][x] = 1
    print(environment)
    print("""PRESS
[1] - UP
[2] - RIGHT
[3] - DOWN
[4] - LEFT""")
    choice = input("INPUT: ")
    if choice == "1" and y != 0:
        y -= 1
    elif choice == "2" and x != columns-1:
        x += 1
    elif choice == "3" and y != rows-1:
        y += 1
    elif choice == "4" and x != 0:
        x -= 1