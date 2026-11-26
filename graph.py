n = 6
e = 7

edge = [(0,1),(0,3),(0,4),(1,2),(1,5),(2,4),(3,4)] #edges

print(edge)

#AdjecentList
adjList =[]

for i in range(n):
    adjList.append([])
    

for item in edge:
    x = item[0]
    y = item[1]
    adjList[x].append(y)
    adjList[y].append(x)

for i in range(n):
    print(i,"->",adjList[i])