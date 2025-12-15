# sum = 0

# with open("test.txt") as f:
#     for line in f:
#         firstSmallestPos = 0
#         secondSmallestPos = 1
#         thirdSmallestPos = 2

#         print("Linelength:",len(line))
#         print(line[firstSmallestPos])
#         for x in range(3,len(line)-2):
#             if line[x] < line[firstSmallestPos]:
#                 print("huh")
#                 thirdSmallestPos = secondSmallestPos
#                 secondSmallestPos = firstSmallestPos
#                 firstSmallestPos = x
#             elif line[x] < line[secondSmallestPos]:
#                 thirdSmallestPos = secondSmallestPos
#                 secondSmallestPos = x
#             elif line[x] < line[thirdSmallestPos]:
#                 thirdSmallestPos = x
#         line[firstSmallestPos]= 0
#         line[secondSmallestPos]= 0
#         line[thirdSmallestPos]= 0

#         for y in range(0,len(line)-2):
#             pass


#         print("Firstlargestpos:",firstSmallestPos, line[firstSmallestPos])
#         print("Secondlargestpos:",secondSmallestPos, line[secondSmallestPos])
#         print("Thirdlargestpos:",thirdSmallestPos, line[thirdSmallestPos])

# print("Final:",sum)ä

sum = 0

with open("input.txt") as f:
    for line in f:
        line = line.strip()
        pos_in_str = 0
        stringy = "000000000000"
        print("Linelength:", len(line))
        for x in range(0, len(line) ):
            # print("Checking:", x, line[x])
            pos_in_str = 0
            while pos_in_str < 12:
                if (line[x] > stringy[pos_in_str]) & (
                    (len(line) - x >= (12 - pos_in_str))
                ):
                    # print(len(line) - (12 - pos_in_str))
                    stringy = (
                        stringy[:pos_in_str] + line[x] + (len(stringy[pos_in_str:]) -1) * "0"
                    )
                    print("test", stringy)
                    pos_in_str = 0
                    break
                pos_in_str = pos_in_str + 1
        print("Stringy now:",stringy)
        sum = sum + int(stringy)

print("Final:", sum)
