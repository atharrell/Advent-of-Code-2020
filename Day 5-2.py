import math
f = open("C:\\Users\\Alex\\Desktop\\Advent of Code 2020\\input.txt", "r")
grid = [line for line in f]

def process(top, bottom, input):
    if input[0] == 'F' or input[0] == 'L':
        top = top - math.ceil((top - bottom) / 2)
        if top == bottom:
            return top
        else:
            return process(top,bottom,input[1:])
    elif input[0] == 'B' or input[0] == 'R':
        bottom = bottom + math.ceil((top - bottom) / 2)
        if top == bottom:
            return top
        else:
            return process(top,bottom,input[1:])
seat_ids = []
for line in grid:
    seat_ids.append(process(127,0,line[0:7])*8 + process(7,0,line[7:10]))
seat_ids.sort()
last = min(seat_ids) - 1
for id in seat_ids:
    if id != last + 1:
        print(id-1)
    last = id