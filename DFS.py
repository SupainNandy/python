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
edge2 = [(0, 1), (0, 3), (0, 4), (1, 2), (1, 5), (2, 4), (3, 4)]

#create Adjuscent list
adjList=[[] for _ in range(n)]
for item in edge2:
    x = item[0]
    y = item[1]

    adjList[x].append(y)
    adjList[y].append(x)
#

s = Stack()
visited  = [False]*n

ans=[]

s.push(0)
visited[0]=True

while s.size()>0:
    node = s.pop()
    ans.append(node)

    for x in adjList[node]: 
        if not visited[x]:
            s.push(x)
            visited[x]=True
print("Adjucent List")
for i in range(n):
    print(i,"->",adjList[i])

print("DFS")
print(ans)


#Recursion 
ans2=[]
visited2=[False]*n
def dfs(i,adjList,visited2):
    visited2[i]=True
    ans2.append(i)

    for x in adjList[i]:
        if not visited2[x]:
            dfs(x,adjList=adjList,visited2=visited2)


print("DFS using recursion")
dfs(0,adjList=adjList,visited2=visited2)
print(ans2)

