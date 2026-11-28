class Queue:
    def __init__(self):
        self.q = []
        self.front = -1

    def push(self, i):
        if self.front == -1:
            self.front = 0
        self.q.append(i)

    def pop(self):
        if self.front == -1 or self.front >= len(self.q):
            return -1
        x = self.q[self.front]
        self.front += 1
        if self.front == len(self.q):
            self.front = -1
            self.q = []
        return x

    def getFront(self):
        if self.front == -1:
            return -1
        return self.q[self.front]

    def size(self):
        if self.front == -1:
            return 0
        return len(self.q) - self.front


#Here the graph
n = 6
e = 7
edge2=  [(0,1),(0,3),(0,4),(1,2),(1,5),(2,4),(3,4)] #edges

adjMatix=[]
adjList=[[] for _ in range(n)]

#Implement adjuscent list
for item in edge2:
    x = item[0]
    y = item[1]

    adjList[x].append(y)
    adjList[y].append(x)

#implement adjucent matrix
for i in range(n):
    adjMatix.append([-1]*n)

for i in edge2:
    a = i[0]
    b = i[1]

    adjMatix[a][b]=1
    adjMatix[b][a]=1
print("Adjuscent Matrix")
for i in adjMatix:
    print(i)

print("Adjuscent List")
for i in range(n):
    print(i,"->",adjList[i])



#implement BFS
q = Queue()

#first we take visited array -> its sizw == numbber or nodes-> and initial value is declear is false
visited = [False]*n
ans=[]
 

q.push(0)
visited[0]=True
ans.append(0)

while q.size()>0:
    front = q.pop()
    for x in adjList[front]:
        if not visited[x]:
            q.push(x)
            visited[x] = True
            ans.append(x)
        
        
    


print("BFS")
print(ans)