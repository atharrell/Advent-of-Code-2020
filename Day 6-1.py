f = open("C:\\Users\\Alex\\Desktop\\Advent of Code 2020\\input.txt", "r")
grid = [line for line in f]

grid.append("\n")
group = ""
total = 0
for line in grid:
    if line == "\n":
        total += len(set(group))
        group = ""
    else:
        group = group + line.strip("\n")
print(total)