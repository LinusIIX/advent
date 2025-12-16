sum = 0
ranges = []

# low: 269857976379192
# richtig: 350939902751909
# high:351482256826440
# high:351607372158882


def smalify(ranges):
    trying = True
    while trying:
        for i in range(len(ranges)):
            for j in range(len(ranges)):
                if i == j:
                    continue
                if (ranges[j][0] <= ranges[i][1] and ranges[j][0] >= ranges[i][0]) or (
                    ranges[j][1] >= ranges[i][0] and ranges[j][1] <= ranges[i][1]
                ):
                    print("merging", ranges[i], ranges[j])
                    ranges[i][0] = min(ranges[j][0], ranges[i][0])
                    ranges[i][1] = max(ranges[j][1], ranges[i][1])
                    ranges.pop(j)
                    break
            else:
                continue
            break
        trying = False
        print("numranges", len(ranges))
        return ranges


with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
        if line.strip() == "":
            break

        [start, end] = line.strip().split("-")
        start = int(start)
        end = int(end)
        ranges.append([start, end])
        # ranges = smalify(ranges)
    # print(ranges)
    previous = len(ranges)
    merging = True
    while merging: #bissl janky aber geht
        ranges = smalify(ranges)
        if len(ranges) == previous:
            merging = False
        else:
            previous = len(ranges)

    # print(ranges)
    for thing in ranges:
        sum += thing[1] - thing[0] + 1

print("Final:", sum)
