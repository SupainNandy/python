class Stack:
    def __init__(self):
        self.s = []

    def push(self, x):
        self.s.append(x)

    def pop(self):
        if len(self.s) == 0:
            return -1
        return self.s.pop()

    def top(self):
        if len(self.s) == 0:
            return -1
        return self.s[-1]

    def size(self):
        return len(self.s)


n = 6
edge = [(0, 1), (0, 3), (0, 4), (1, 2), (1, 5), (2, 4), (3, 4)]



#craete Adjuscent list
adjList=[]
adjList2 = [
    [1,3],
    [0,2],
    [1],
    [0],
    [0]
]

# create Adjacent list
for item in range(n):
    adjList.append([])

for i in edge:
    x = i[0]
    y = i[1]

    adjList[x].append(y)
    adjList[y].append(x)

for i in range(n):
    print(i,"->",adjList[i])


# Dfs implement 
visited = [False]*n
def dfs(i, parent, adjList, visited):
    visited[i] = True

    for x in adjList[i]:
        if x == parent:
            continue
        if visited[x]:
            return True
        if dfs(x, i, adjList, visited):
            return True

    return False


print("Cycle detected using DFS:")
print(dfs(0, -1, adjList=adjList2, visited=visited))
