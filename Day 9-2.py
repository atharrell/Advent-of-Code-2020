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
        for i in range(0,len(numbers)):
            counter = 0
            arr = []
            if numbers[i] != num:
                for j in range(i,len(numbers)):
                    counter += numbers[j]
                    arr.append(numbers[j])
                    if counter == num:
                        arr.sort()
                        print(arr[0] + arr[len(arr) - 1])
                        break
        break
    upper += 1
    lower += 1