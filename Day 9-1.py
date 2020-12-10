f = open("C:\\Users\\Alex\\Desktop\\Advent of Code 2020\\input.txt", "r")
numbers = [int(line.strip('\n')) for line in f]
right = numbers[25:]
lower = 0
upper = 25
for num in right:
    left = numbers[lower:upper]
    left = set(left)
    found = False
    for num2 in left:
        if num - num2 in left:
            found = True
            break
    if not found:
        print(num)
        break
    upper += 1
    lower += 1