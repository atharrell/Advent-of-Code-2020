f = open("C:\\Users\\Alex\\Desktop\\Advent of Code 2020\\input.txt", "r")
numbers = [int(number) for number in f]
for n1 in numbers:
    for n2 in numbers:
        for n3 in numbers:
            if n1 != n2 and n2 != n3 and n1 != n3:
                if n1 + n2 + n3 == 2020:
                    print(n1*n2*n3)
                    break