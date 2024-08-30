class Queue:
    def __init__(self,capacity):
        self.queue = []
        self.capacity = capacity
    def isEmpty(self):
        return self.size() == 0
    def isFull(self):
        return self.size() >= capacity
    def size(self):
        return len(self.queue)
    def enqueue(self,data):
        if self.isFull():
            print("已滿")
            return
        self.queue.append(data)
    def dequeue(self):
        if self.isEmpty():
            print("已空")
            return None
        return self.queue.pop(0)
    
    
