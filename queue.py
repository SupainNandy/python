class Queue:
    def __init__(self):
        self.arr = []

    #insert element
    def  enqueue(self,data):
        self.arr.append(data)
        print("Inserted")

    #Delete element in array
    def delete(self):
        if self.isEmpty():
            print("Queue is empty")
            return

        removed=self.arr.pop(0)
        print(removed,"Element delete successfuly")


    #Get  front element
    def get_Element(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        print("Front element: ",self.arr[0])

    #Display all Queue
    def display(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        print("Queue: ",self.arr)

    #ISEmpty queue
    def isEmpty(self):
        return len(self.arr) == 0



q=Queue()
q.enqueue(10)
q.enqueue(20)
print("Display all Queue")
q.display()
print("Get front element")
q.get_Element()
q.enqueue(30)
print("Display all Queue")
q.display()
print("Delete element")
q.delete()
print("Display all Queue")
q.display()

        

        


    