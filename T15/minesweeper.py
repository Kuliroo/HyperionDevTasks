# Program which takes 2d-list of '-' and '#', and returns 2d-list showing how many
# '#' each '-' neighbours
import copy
# entry grid for the program
entry_grid = [  ["-", "-", "-", "#", "#"],
                ["-", "#", "-", "-", "-"],
                ["-", "-", "#", "-", "-"],
                ["-", "#", "#", "-", "-"],
                ["-", "-", "-", "-", "-"] ]


# preparing a spare grid to operate on
new_grid = copy.copy(entry_grid)
rows = len(new_grid)

# nested for loop with coordinates in try loop to check if each '-' borders any '#'
for row in range(rows):
    cols = len(new_grid[row])
    for col in range(cols):
        if new_grid[row][col] == "-":
            try:
                mines = 0
                if row-1 >= 0 and col-1 >= 0 and new_grid[row-1][col-1] == "#":
                    mines += 1
                if row-1 >= 0 and new_grid[row-1][col] == "#":
                    mines += 1
                if row-1 >= 0 and col+1 < cols and new_grid[row-1][col+1] == "#": 
                    mines += 1
                if col-1 >= 0 and new_grid[row][col-1] == "#":                      
                    mines += 1
                if col+1 < cols and new_grid[row][col+1] == "#":
                    mines += 1
                if row+1 < rows and col-1 >= 0 and new_grid[row+1][col-1] == "#":
                    mines += 1
                if row+1 < rows and new_grid[row+1][col] == "#":
                    mines += 1
                if row+1 < rows and col+1 < cols and new_grid[row+1][col+1] == "#":
                    mines += 1
                new_grid[row][col] = str(mines)
            except IndexError:
                continue
# returning printed 2d-list             
for row in range(rows):
    print(new_grid[row])