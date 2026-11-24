import heapq

#Min heap implementation using heapq module

pq = []  # Create an empty priority queue


heapq.heappush(pq,30)
heapq.heappush(pq,10)
heapq.heappush(pq,50)
heapq.heappush(pq,20)

print("Display all Queue")
print(pq)


#Remove smallest element
print("Remove smallest element")
heapq.heappop(pq)
print("Queue after removing smallest element")
print(pq)

#Max heap implementation using heapq module
pq1 = []

heapq.heappush(pq1, -30)
heapq.heappush(pq1, -10)
heapq.heappush(pq1, -50)
heapq.heappush(pq1, -20)

print(-heapq.heappop(pq1))  # 50
print(-heapq.heappop(pq1))  # 30
print(-heapq.heappop(pq1))  # 20


#Coustom Priority queue implementation using heapq module

coustom = []

heapq.heappush(coustom, (3, "Normal Fever"))
heapq.heappush(coustom, (1, "Heart Attack"))
heapq.heappush(coustom, (2, "Fracture"))

while coustom:
    priority, patient = heapq.heappop(coustom)
    print(f"Patient: {patient}, Priority: {priority}")
    