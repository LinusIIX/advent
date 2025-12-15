
sum = 0

with open("input.txt") as f:
    for line in f:
        firstlargest = line[0]
        print("Linelength:",len(line))
        secondlargest = -1
        print("Firstlargest:",firstlargest)
        for x in range(1,len(line)-1):
            print("Checking:",x,line[x])
            if ((line[x] > firstlargest) & (x != len(line)-2)):
                firstlargest = line[x]
                secondlargest = -1
            elif (int(line[x]) > int(secondlargest)):
                secondlargest = line[x]
                
        sum = sum + 10*int(firstlargest) + int(secondlargest)
        print("Firstlargest:",firstlargest)
        
        print("Secondlargest:",secondlargest)

print("Final:",sum)