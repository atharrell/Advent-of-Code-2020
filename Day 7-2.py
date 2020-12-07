import re
f = open("C:\\Users\\Alex\\Desktop\\Advent of Code 2020\\input.txt", "r")
parse_inside_bags = re.compile(r"(\d+)((?:[a-z]|\s)*)(?:bag|bags)(?:,|.)")
parse_outside_bag = re.compile(r"(\w+\s\w+)\s(?:bag|bags)\scontain")

rules = {}
count = 0
for line in f:
    inside_bags = parse_inside_bags.findall(line)
    outside_bag = parse_outside_bag.match(line)
    rules[outside_bag[1]] = inside_bags

def russian_doll_search(key):
    return sum([russian_doll_search(tup[1].strip())*int(tup[0]) + int(tup[0]) for tup in rules[key]])

print(russian_doll_search("shiny gold"))