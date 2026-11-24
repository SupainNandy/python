from collections import deque

dq = deque()

# Insert drom rear
dq.append(10)
dq.append(20)
dq.append(30)
dq.append(40)

print("Display all Queue")
print(dq)

print("Insert element from front")
dq.appendleft(5)
print(dq)

print ("Delete element from rear")
dq.pop()
print(dq)

print("Delete element from front")
dq.popleft()
print(dq)

print("Get front element")
print("Front element: ",dq[0])

print("Get rear element")
print("Rear element: ",dq[-1])