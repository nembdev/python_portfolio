grid = [
    [".", ".", ".", ".", ".", "."],
    [".", "O", "O", ".", ".", "."],
    ["O", "O", "O", "O", ".", "."],
    ["O", "O", "O", "O", "O", "."],
    [".", "O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O", "."],
    ["O", "O", "O", "O", ".", "."],
    [".", "O", "O", ".", ".", "."],
    [".", ".", ".", ".", ".", "."],
]

# loop through x,y
for x in range(6):
    for y in range(9):
        # print in "reverse" y, x
        # if we're not at the end, don't add a newline
        if y < 8:
            print(grid[y][x], end="")
        else:
            print(grid[y][x])
