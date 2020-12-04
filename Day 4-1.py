import re

parser = re.compile(r"(?=.*byr:)(?=.*iyr:)(?=.*eyr:)(?=.*hgt:)(?=.*hcl:)(?=.*ecl:)(?=.*pid:)",flags=re.I|re.S)
f = open("C:\\Users\\Alex\\Desktop\\Advent of Code 2020\\input.txt", "r")
grid = [line for line in f]
grid.append("\n")
full_passport = ""
full_passports = 0
for line in grid:
    if line == "\n":
        if parser.match(full_passport) != None:
            full_passports += 1
        full_passport = ""
    else:
        full_passport = full_passport + line.strip("\n") + " "
print(full_passports)