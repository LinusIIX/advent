
circuits = []
nodes = []
distances = []

def distance(point1,point2):
    return abs((point1[0]) - (point2[0])) + abs((point1[1]) - (point2[1]))+ abs((point1[2]) - (point2[2]))

with open("test.txt") as f:
    lines = f.readlines()
    for line in lines:
        if line.strip() == "":
            break
        line = line.strip()
        X,Y,Z = line.split(",")
        nodes.append([int(X),int(Y),int(Z)])
print(len(nodes))
for node1 in range(len(nodes)):
    print("Progress",(node1/(len(nodes))),"%")
    for node2 in range(node1,len(nodes)):
        if node1 == node2:
            continue
        if [nodes[node2],nodes[node1],distance(nodes[node2],nodes[node1])] in distances:
            pass
        else:
            distances.append([nodes[node1],nodes[node2],distance(nodes[node1],nodes[node2])])
        
    distances = sorted(distances,reverse=False,key=lambda distancey: distancey[2])
    while len(distances) > 10:
        distances.pop()       
    
for thing in distances:
    found_circuit_id = -1
    for circuit_id in range(len(circuits)):
        if circuit_id != -1:
            if thing[0] in circuits[circuit_id]:
                circuits[circuit_id].append(thing[1])
                found_circuit_id = circuit_id
            elif thing[1] in circuits[circuit_id]:
                circuits[circuit_id].append(thing[0])
                found_circuit_id = circuit_id
        else:
            if thing[0] in circuits[circuit_id]:
                circuits[circuit_id].remove(thing[0])
                circuits[found_circuit_id].append(circuits[circuit_id])
                circuits.remove(circuits[circuit_id])
            elif thing[1] in circuits[circuit_id]:
                circuits[circuit_id].remove(thing[1])
                circuits[found_circuit_id].append(circuits[circuit_id])
                circuits.remove(circuits[circuit_id])
    if found_circuit_id == -1:
        circuits.append([thing[0],thing[1]])        
circuits.sort(reverse=True,key=len)
while len(circuits) > 10:
    circuits.pop()
    print("hiu")
    
#print("Finally:",circuits)

for bla in circuits:
    print(bla)
    print("length",len(bla))