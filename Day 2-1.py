import re

f = open("C:\\Users\\Alex\\Desktop\\Advent of Code 2020\\input.txt", "r")
parser = re.compile(r"(\d+)-(\d+)\s(\S):\s(.*)")
matches = [parser.match(line) for line in f]
print(sum([1 for match in matches if int(match[1]) <= match[4].count(match[3]) <= int(match[2])]))