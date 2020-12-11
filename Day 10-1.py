f = open("C:\\Users\\Alex\\Desktop\\Advent of Code 2020\\input.txt", "r")
adapters = [int(line.strip('\n')) for line in f]
adapters.sort()
adapters.insert(0,0)
adapters.append(max(adapters) + 3)
ones, threes = 0, 0
for i in range(0,len(adapters)):
    if adapters[i] - adapters[i-1] == 1:
        ones += 1
    elif adapters[i] - adapters[i-1] == 3:
        threes += 1
print(ones*threes)