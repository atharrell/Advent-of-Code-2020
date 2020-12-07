import re
f = open("C:\\Users\\Alex\\Desktop\\Advent of Code 2020\\input.txt", "r")
parse_inside_bags = re.compile(r"\d+((?:[a-z]|\s)*)(?:bag|bags)(?:,|.)")
parse_outside_bag = re.compile(r"(\w+\s\w+)\s(?:bag|bags)\scontain")

rules = {}
count = 0
for line in f:
    inside_bags = parse_inside_bags.findall(line)
    inside_bags = [bag.strip() for bag in inside_bags]
    outside_bag = parse_outside_bag.match(line)
    rules[outside_bag[1]] = inside_bags

def russian_doll_search(key):
    if "shiny gold" in rules[key]:
        return True
    else:
        search_results = [russian_doll_search(new_key) for new_key in rules[key]]
        if True in search_results:
            return True

for key in rules.keys():
    if russian_doll_search(key):
        count += 1
print(count)