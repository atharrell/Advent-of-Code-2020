f = open("C:\\Users\\Alex\\Desktop\\Advent of Code 2020\\input.txt", "r")
grid = [line for line in f]
paths = [[1,1],[3,1],[5,1],[7,1],[1,2]]
multiplied = 1

def get_trees_hit(x_inc, y_inc):
    pos_x = 0
    pos_y = 0
    trees_hit = 0
    row_len = len(grid[0]) - 1
    while (pos_y != len(grid)-1):
        pos_x += x_inc
        pos_y += y_inc
        if grid[pos_y][pos_x % row_len] == '#':
            trees_hit += 1
    return trees_hit

for path in paths:
    multiplied *= get_trees_hit(path[0], path[1])
print(multiplied)