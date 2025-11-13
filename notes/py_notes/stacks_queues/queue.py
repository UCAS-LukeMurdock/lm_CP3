
class Queue:
    def __init__(self):
        self.queue = []
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            self.queue.pop(0)
        else:
            return None
    
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
    
    def size(self):
        return len(self.queue)