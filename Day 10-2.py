f = open("C:\\Users\\Alex\\Desktop\\Advent of Code 2020\\input.txt", "r")
adapters = [int(line.strip('\n')) for line in f]
adapters.sort()
adapters.append(max(adapters) + 3)
last, consecutive = 0, 0
counts = [0,0,0,0,0]
for adapter in adapters:
    delta = adapter - last
    if delta == 1:
        consecutive += 1
    elif delta == 3:
        counts[consecutive] += 1
        consecutive = 0
    last = adapter
print(2**counts[2] * 4**counts[3] * 7**counts[4])