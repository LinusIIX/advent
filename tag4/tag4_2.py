sum = 0
sumy = 1
change = True
checklines = []


def check_middle():
    global checklines
    summerizer = 0
    tester = checklines[1]
    for x in range(len(checklines[1])):
        if checklines[1][x] == "@":
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
                if x + i[1] < 0 or x + i[1] >= len(checklines[1]):
                    continue
                if checklines[1 + i[0]][x + i[1]] == "@":
                    checker = checker + 1
            tester = tester[:x] + "@" + tester[x + 1 :]
            if checker < 4:
                checklines[1] = checklines[1][:x] + "x" + checklines[1][x + 1 :]
                # tester = tester[:x] + "x" + tester[x + 1 :]
                summerizer = summerizer + 1
    print("Summerizer now:", summerizer)
    print("Tester now:", checklines[1])
    return summerizer


with open("input.txt") as f:
    lines = f.readlines()
    while sumy > 0:
        sumy = 0
        runs = -1
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
            sumy += check_middle()
            if runs >= 0:
                lines[runs] = checklines[1]
            runs = runs + 1
            if line == lines[-1]:
                checklines.pop(0)
                checklines.append(len(line) * ".")
                print("Processing line:", checklines[1])
                sumy += check_middle()
                lines[runs] = checklines[1]
        sum = sum + sumy
            # print("Checklines now:",checklines)

print("Final:", sum)
