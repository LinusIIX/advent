sum = 0
#have all prevous splits in this array so i can go back and explore the other side(only on going left and then delete when jumping to it and going right)
previous_splits=[(0,0)]


with open("input.txt") as f:
    lines = f.readlines()
    for j in range(len(lines)):
        lines[j].strip()
        lines[j] = lines[j].split()

    for i in range(1,len(lines)):
        for j in range(0,len(lines[0])):
            print(lines[i-1][j])
            if lines[i-1][j] == "|" or "S":
                if lines[i][j] == "^":
                    sum = sum + 1
                    lines[i][j+1] = "|"
                    lines[i][j-1] = "|"
                    print("test")
                else:    
                    lines[i][j] = "|"
        
print("Finall:",sum)