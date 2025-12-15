
sum = 0


def halfable(x):
    if len(x) % 2 != 0:
        return False
    länge = int(len(x))
    halbelänge = int(länge/2)
    return x[0:halbelänge] == x[halbelänge:länge]
    
        

with open("input.txt") as f:
    
    line = f.readline()
    splitted = line.split(",")
    for x in splitted:
        pos,pos2 = x.split("-")
        print(pos,pos2)
        for i in range(int(pos),int(pos2)+1):
            if halfable(str(i)):
                sum += i
                print(i)
                
print("Final: ",sum)