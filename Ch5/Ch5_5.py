class Queue:
    def  __init__(self):
        self.my_queue = []
    def enqueue(self,data):
        self.my_queue.append(data)
    def dequeue(self):
        return self.my_queue.pop(0)
    def size(self):
        return len(self.my_queue)
    def isEmpty(self):
        return self.size() == 0
queue = Queue() 
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")
while not queue.isEmpty():
    print(queue.dequeue())
