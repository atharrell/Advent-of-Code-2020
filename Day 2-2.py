import re

f = open("C:\\Users\\Alex\\Desktop\\Advent of Code 2020\\input.txt", "r")
parser = re.compile(r"(\d+)-(\d+)\s(\S):\s(.*)")
matches = [parser.match(line) for line in f]
total = 0
for match in matches:
    count = 0
    try:
        if match[4][int(match[1]) - 1] == match[3]:
            count += 1
    except:
        pass
    try:
        if match[4][int(match[2]) - 1] == match[3]:
            count += 1
    except:
        pass
    if count == 1:
        total += 1
print(total)