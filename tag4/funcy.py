
lines = [1, 2, 3, 4, 5]
y = 0
for i in lines:
    lines[y]= i * 2
    i = i + 1
    y+=1
    
print(lines)