sum = 0
topping = True
ranges = []

with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
        if line.strip() == "":
            topping = False
        elif topping:
            [start,end] = line.strip().split("-")
            start = int(start)
            end = int(end)
            ranges.append([start,end])
        else:
            num = int(line.strip())
            allowed = False
            for r in ranges:
                if (num >= r[0]) & (num <= r[1]):
                    allowed = True
            if allowed:
                sum = sum + 1
        
print("Final:",sum)