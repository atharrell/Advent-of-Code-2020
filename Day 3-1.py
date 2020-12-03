f = open("C:\\Users\\Alex\\Desktop\\Advent of Code 2020\\input.txt", "r")
grid = [line for line in f]
pos_x = 0
pos_y = 0
trees_hit = 0
row_len = len(grid[0]) - 1
while (pos_y != len(grid)-1):
    pos_x += 3
    pos_y += 1
    if grid[pos_y][pos_x % row_len] == '#':
        trees_hit += 1

print(trees_hit)