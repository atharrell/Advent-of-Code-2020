from collections import Counter
f = open("C:\\Users\\Alex\\Desktop\\Advent of Code 2020\\input.txt", "r")
grid = [line for line in f]

grid.append("\n")
group = ""
count = 0
total = 0
for line in grid:
    if line == "\n":
        total += len([value for value in Counter(group).values() if value == count])
        count = 0
        group = ""
    else:
        group = group + line.strip("\n")
        count += 1
print(total)