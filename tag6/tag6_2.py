sum = 0

def col_empty(lines,x):
    aggregator = True
    for i in range(len(lines) - 1):
        aggregator = aggregator and (lines[i][x] == ' ')
    return aggregator

with open("input.txt") as f:
    lines = f.readlines()
    operation = lines[-1][0]
    summerizer = 1
    print(operation)
    for i in range(len(lines[0])):
        if(lines[0][i]== '\n'):
            sum += summerizer
            
        elif(col_empty(lines,i)):
            print("colum empty:",i)
            print("summerizer",summerizer)
            sum += summerizer
            summerizer = 0
            operation = lines[-1][i+1]
            if operation == "*":
                summerizer = 1
            print(operation)
        else:
            number = ""
            for j in range(len(lines)-1):
                number += lines[j][i]
            print("number",number)
            if operation == "+":
                summerizer += int(number)
            else:
                summerizer *= int(number)
            
        
        # sum += result

print("Finall:", sum)
