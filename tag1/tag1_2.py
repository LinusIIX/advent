
import math
current = 50
nullen = 0
#nicht 6967,6980,7077

with open("input.txt") as f:
  for x in f:
    if x.startswith("R"):
        change = int(x.split("R")[1])
        if change > 99 - current:
            nullen += math.floor((change + current)/ 100)
            #print(nullen)
        current = (current + change)%100
    elif x.startswith("L"):
        change = int(x.split("L")[1])
        if change >= current:
            nullen += math.floor((change - current)/100) + 1
            if current == 0:
                nullen -= 1
            print(current,change," ", math.floor((change - current)/100) + 1)
        current = (current - change)%100
    
    # if current == 0:
    #     print("test")
    #     #nullen += 1
    
print("Final: ",nullen)