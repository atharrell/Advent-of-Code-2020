import copy
f = open("C:\\Users\\Alex\\Desktop\\Advent of Code 2020\\input.txt", "r")
grid = [{"instruction": line.strip('\n'), "run": 0} for line in f]
grid_copy = copy.deepcopy(grid)
idx = 0
initial_path = []

while(grid[idx]["run"] != 1):
    split = grid[idx]["instruction"].split(' ')
    if split[0] == 'acc':
        grid[idx]["run"] = 1
        idx += 1
    elif split[0] == 'nop':
        grid[idx]["run"] = 1
        idx += 1
    elif split[0] == 'jmp':
        grid[idx]["run"] = 1
        idx += int(split[1])
    initial_path.append(grid[idx])
initial_path.reverse()

for point in initial_path:
    grid = copy.deepcopy(grid_copy)
    idx = 0
    for a in grid:
        if a["instruction"] == point["instruction"]:
            break
        idx += 1
    split = point["instruction"].split(' ')
    if split[0] == 'nop':
        grid[idx] = {"instruction": 'jmp' + ' ' + split[1], "run": 0}
    elif split[0] == 'jmp':
        grid[idx] = {"instruction": 'nop' + ' ' + split[1], "run": 0}

    total = 0
    idx = 0

    while(idx != len(grid) - 1 and grid[idx]["run"] != 1):
        split = grid[idx]["instruction"].split(' ')
        if split[0] == 'acc':
            total += int(split[1])
            grid[idx]["run"] = 1
            idx += 1
        elif split[0] == 'nop':
            grid[idx]["run"] = 1
            idx += 1
        elif split[0] == 'jmp':
            grid[idx]["run"] = 1
            idx += int(split[1])
    if (grid[idx]["run"] != 1):
        print(total)
        break