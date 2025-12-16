sum = 0

checklines = []


def check_middle(lines):
    summerizer = 0
    tester = lines[1]
    for x in range(len(lines[1])):
        if lines[1][x] == "@":
            checker = 0
            for i in [
                [-1, -1],
                [-1, 0],
                [-1, 1],
                [0, -1],
                [0, 1],
                [1, -1],
                [1, 0],
                [1, 1],
            ]:
                if x + i[1] < 0 or x + i[1] >= len(lines[1]):
                    continue
                if lines[1 + i[0]][x + i[1]] == "@":
                    checker = checker + 1
            if checker < 4:
                summerizer = summerizer + 1
    print("Summerizer now:", summerizer)
    print("Tester now:", tester)
    return summerizer


with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:

        line = line.strip()
        if len(checklines) == 0:
            checklines.append(len(line) * ".")
            checklines.append(len(line) * ".")
            checklines.append(line)
        else:
            checklines.pop(0)
            checklines.append(line)
        print("Processing line:", checklines[1])
        sum += check_middle(checklines)

        if line == lines[-1]:
            checklines.pop(0)
            checklines.append(len(line) * ".")
            print("Processing line:", checklines[1])
            sum += check_middle(checklines)

        # print("Checklines now:",checklines)

print("Final:", sum)
