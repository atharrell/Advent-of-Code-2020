import re

parser = re.compile(r"(?=.*byr:(19[2-9][0-9]|200[0-2])\s)(?=.*iyr:(201[0-9]|2020)\s)(?=.*eyr:(202[0-9]|2030)\s)(?=.*hgt:(1[5-8][0-9]cm|19[0-3]cm|7[0-6]in|6[0-9]in|59in)\s)(?=.*hcl:#([0-9]|[a-f]){6}\s)(?=.*ecl:(amb|blu|brn|gry|grn|hzl|oth)\s)(?=.*pid:([0-9]){9}\s)",flags=re.I|re.S)
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