import math

sum = 0


def choping(x):
   
    länge = int(len(x))
    chuncksize = int(länge/2)
    while chuncksize > 0:
        first = x[0:chuncksize]
        checker = True
        for i in range(1, int(math.ceil(länge/chuncksize))):
            if first != x[i*chuncksize:(i+1)*chuncksize]:
                print("first",first,"different:",x[i*chuncksize:(i+1)*chuncksize],"i",i)
                checker = False
                break
        if checker:
            print("repeting:",first,"number:",x)
            return True
        chuncksize -= 1
    return False
    # halbelänge = int(länge/2)
    # return x[0:halbelänge] == x[halbelänge:länge]
    
        

with open("input.txt") as f:
    line = f.readline()
    splitted = line.split(",")
    for x in splitted:
        pos,pos2 = x.split("-")
        print(pos,pos2)
        for i in range(int(pos),int(pos2)+1):
            if choping(str(i)):
                sum += i
                print(i)
                
print("Final: ",sum)


