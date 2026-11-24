class PriorityQueue:
    def __init__(self):
        self.heap=[]

    #check Parent index
    def parent(self,i):
        return (i-1)//2

    #Check Left child index
    def left_Child(self,i):
        return 2*i+1

    #Check Right childd index
    def right_child(self,i):
        return 2*i-1

    #Swap Two element
    def swap(self,i,j):
        self.heap[i], self.heap[j] = self.heap[j],self.heap[i]

    # Insert element
    def insert(self, value):

        self.heap.append(value)

        self.heapify_up(len(self.heap) - 1)

    # Maintain heap property after insertion
    def heapify_up(self,i):
        while i > 0:
            parent_index = self.parent(i)
            if self.heap[i] < self.heap[parent_index]:
                self.swap(i,parent_index)

                i = parent_index

            else:
                break

    #Return smallest element
    def peek(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    #remove smallest element
    def extract_min(self):
        if len(self.heap)==0:
            return None

        minimum = self.heap[0]

        self.heap[0]=self.heap.pop()

        self.heapify_down(0)

        return minimum

    def heapify_down(self,i):
        size=len(self.heap)

        while True:
            smallest = i

            left=self.left_Child(i)
            right=self.right_child(i)

            if left < size and self.heap[left] < self.heap(smallest):
                smallest=right
            if smallest != i:
                self.swap(i,smallest)
                i= smallest
            else:
                break


        # Display heap
    def display(self):
        print("Heap:", self.heap)

         # Return size
    def size(self):
        return len(self.heap)

    # Check empty
    def is_empty(self):
        return len(self.heap) == 0



    # Testing

pq = PriorityQueue()

pq.insert(40)
pq.insert(20)
pq.insert(50)
pq.insert(10)
pq.insert(30)

pq.display()
                