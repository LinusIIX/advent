sum = 0


with open("input.txt") as f:
    lines = f.readlines()
    for j in range(len(lines)):
        lines[j].strip()
        lines[j] = lines[j].split()

    for i in range(len(lines[0])):
        result = int(lines[0][i])
        for j in range(1,len(lines)-1):
            if lines[-1][i] == "+":
                result+= int(lines[j][i])
            else:
                result *= int(lines[j][i])
            
            
        sum += result
        
print("Finall:",sum)