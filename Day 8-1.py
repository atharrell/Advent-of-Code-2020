f = open("C:\\Users\\Alex\\Desktop\\Advent of Code 2020\\input.txt", "r")
grid = [{"instruction": line.strip('\n'), "run": 0} for line in f]
idx = 0
total = 0

while(grid[idx]["run"] != 1):
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

print(total)