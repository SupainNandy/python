class Maxheap:
    def __init__(self):
        self.heap=[]

    def parent(self,i):
        return (i-1)//2

    def left_child(self,i):
        return 2 * i + 1

    def right_child(self,i):
        return i*2+2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def size(self):
        return len(self.heap)

    def peek(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    #push and Heapify
    def push(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap)-1)

    def _heapify_up(self, i):
        while i > 0:
            p = self.parent(i)
            if self.heap[i] > self.heap[p]:
                self.swap(i, p)
                i = p
            else:
                break


    def pop(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        max_val = self.heap[0]
        # Last element ko root par le aao
        self.heap[0] = self.heap.pop()
        # Niche correct position par bhejo
        self._heapify_down(0)
        return max_val

    def _heapify_down(self, i):
        size = len(self.heap)
        while True:
            largest = i
            left = self.left_child(i)
            right = self.right_child(i)

            # Left child bada hai?
            if left < size and self.heap[left] > self.heap[largest]:
                largest = left

            # Right child bada hai?
            if right < size and self.heap[right] > self.heap[largest]:
                largest = right

            # Agar koi child parent se bada nikla toh swap karo
            if largest != i:
                self.swap(i, largest)
                i = largest
            else:
                break


def kth_smallest(arr, k):
    max_heap = Maxheap()
    for num in arr:
        max_heap.push(num)
        # Agar heap size k se bada ho jaye, toh sabse bada element pop karo
        if max_heap.size() > k:
            max_heap.pop()

    # Heap ke top par Kth smallest element hoga
    return max_heap.peek()

# Example Test
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(f"{k}th smallest element is:", kth_smallest(arr, k)) # Output: 7