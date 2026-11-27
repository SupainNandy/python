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
